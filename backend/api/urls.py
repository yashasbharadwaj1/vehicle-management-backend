app_name = 'api'
from django.urls import path 
from userauths import views as userauth_views 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    # Authentication
    path('user/register/', userauth_views.RegisterView.as_view(), name='auth_register'),
    path('user/login/', userauth_views.LoginView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/logout/',userauth_views.LogoutView.as_view(), name='logout_user'),
]

