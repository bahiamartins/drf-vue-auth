from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


invalid_emails = [
    '@yahoo',
    '@gmail',
    '@hotmail',
    '@outlook',
    '@icloud',
    '@getnada',
    '@amail.club',
    '@banit.club',
    '@banit.me',
    '@cars2.club',
    '@cmail.club',
    '@nada.email',
    '@nada.ltd',
    '@wmail.club',
    '@mail.ru',
    '@bk.ru',
    '@inbox.ru',
    '@list.ru',
    'yandex.ru',
    '@protonmail.com',
    '@company.com',
    '@company.com.br',
    '@net.com',
    '@net.com.br',
    '@bol.com.br',
    '@airmailbox',
    '@bol.com',
    '@aol.com',
    '@live.com',
]


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'})
    password_confirm = serializers.CharField(style={'input_type': 'password'})


class UserCreateSerializer(serializers.ModelSerializer):

    email_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'email_confirm',
            'password',
        ]
    
    def validate(self, data):

        if not data['email'] == data['email_confirm']:
            raise serializers.ValidationError(_("Emails digitados não estão idênticos. Verifique."))
        
        for i in invalid_emails:
            if i in data['email']:
                raise serializers.ValidationError(_("Email não permitido. Por favor utilize seu email profissional."))
        
        return data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'is_active',
            'last_login',
        ]