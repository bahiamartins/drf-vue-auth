from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.db import IntegrityError
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _

from threading import Thread

from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from apiauth.serializers import (
    UserCreateSerializer, UserSerializer, PasswordResetSerializer, ChangePasswordSerializer
)

from core.mail import sendEmail

UserModel = get_user_model()


def sendActivationLink(request, user):
    #enviar email
    current_site = get_current_site(request)
    site_name = current_site.name
    domain = current_site.domain

    title = _('Confirme seu cadastro')
    subject = f'{site_name} | {title}'

    uid = urlsafe_base64_encode(force_bytes(str(user.pk)))
    token = token_generator.make_token(user)

    linkFront = f'http://localhost:8080/confirm/email/{uid}/{token}/'

    d = {
        'site_name': site_name,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
        'token': token_generator.make_token(user),
        'linkFront': linkFront
    }

    htmly = get_template('emails/createUser.html')
    html_content = htmly.render(d)
    
    data = {
        'first_name': user.first_name,
        'message': html_content,
        'company': site_name,
    }
    from_email = settings.FROM_EMAIL

    Thread(
        target=sendEmail,
        args=(data, subject, from_email, user.email)
    ).start()


def changePassword(request, user):
    #enviar email
    current_site = get_current_site(request)
    site_name = current_site.name
    domain = current_site.domain

    title = _('Recuperar Senha')
    subject = f'{site_name} | {title}'

    uid = urlsafe_base64_encode(force_bytes(str(user.pk)))
    token = token_generator.make_token(user)

    linkFront = f'http://localhost:8080/password/change/{uid}/{token}/'

    d = {
        'site_name': site_name,
        'domain': domain,
        'uid': uid,
        'token': token,
        'linkFront': linkFront
    }

    htmly = get_template('emails/passwordReset.html')
    html_content = htmly.render(d)
    
    data = {
        'first_name': user.first_name,
        'message': html_content,
        'company': site_name,
    }
    from_email = settings.FROM_EMAIL

    Thread(
        target=sendEmail,
        args=(data, subject, from_email, user.email)
    ).start()


class CreateUser(CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):

        data = serializer.data
        email = data["email"].lower().strip()
        first_name = data["first_name"].title()
        last_name = data["last_name"].title()
        password = data["password"]

        try:
            validate_password(password)
        except:
            raise ValidationError(_("Sua senha precisa ter 8 caracteres no mínimo, além de caracteres especiais, letras e números"))
            
        try:
            user = User.objects.create(
                    username = email,
                    email = email,
                    first_name = first_name,
                    last_name = last_name
                )
            user.set_password(password)
            user.is_active = False
            user.save()

            sendActivationLink(self.request, user)

        except IntegrityError:
            raise ValidationError(_('Email já cadastrado. Favor fazer login.'))


class UserActivateAccount(APIView):

    def get(self, request, *args, **kwargs):

        user_is_active = False
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = UserModel._default_manager.get(pk=uid)
            if user is not None and token_generator.check_token(user, token):
                if not user.is_active:
                    user.is_active = True
                    user.save()
            user_is_active = True
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError(_('Não foi possível ativar a conta.'))
        
        return Response({'user_is_active': user_is_active})


class PasswordReset(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request):

        email = request.data['email'].strip().lower()
        hide_mail = '{}***@{}'.format(email.split("@")[0][:5], email.split("@")[1])
        msg = _('Mensagem enviada para o email {}, caso esteja cadastrado.').format(hide_mail)
        context={'message': msg}

        # check if user exists
        try:
            user = User.objects.get(username=email)
            changePassword(self.request, user)
        except User.DoesNotExist:
            #Usuário não encontrado
            return Response(context)
       
        return Response(context)


class ChangePassword(APIView):
    serializer_class = ChangePasswordSerializer

    def dispatch(self, *args, **kwargs):

        assert 'uidb64' in kwargs and 'token' in kwargs
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            token = kwargs['token']
            if not token_generator.check_token(self.user, token):
                raise ValidationError({'token': ['Invalid value']})
        
        return super().dispatch(*args, **kwargs)


    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            user = None
        return user
    

    def post(self, request, *args, **kwargs):

        msg = _('Senha alterada com sucesso. Faça Login')
        context={
            'message': msg,
            'status': 'Success'
        }

        if request.data['password'] == request.data['password_confirm']:
            user_ = self.get_user(kwargs['uidb64'])
            user_.set_password(request.data['password'])
            user_.is_active = True
            user_.save()
            
        else:
            msg = _('Senhas não conferem. Tente novamente.')
        
            context={
                'message': msg,
                'status': 'Error'
            }
            
        return Response(context)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        try:
            queryset = UserModel._default_manager.get(pk=self.request.user.pk)
            serializer = UserSerializer(queryset)
            return Response(serializer.data)
        except:
            raise ValidationError(_('Nao foi possivel processar sua informação.'))

