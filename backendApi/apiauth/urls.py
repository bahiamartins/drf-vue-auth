
from django.urls import path
from apiauth.views import (
    CreateUser, 
    UserActivateAccount,
    PasswordReset,
    ChangePassword,
    UserView,
)

urlpatterns = [
    path('user/create/', CreateUser.as_view(), name='CreateUser'),
    path('user/activate/<uidb64>/<token>/', UserActivateAccount.as_view(), name='UserActivateAccount'),
    path('password/reset/', PasswordReset.as_view(), name='PasswordReset'),
    path('password/change/<uidb64>/<token>/', ChangePassword.as_view(), name='ChangePassword'),
    path('get/user/', UserView.as_view(), name='UserView'),
]