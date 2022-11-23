from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('rest_framework.urls')),
    path('v1/', include('apiauth.urls')),
    path('v1/login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]