from django.urls import path
from .views import login_view, logout_view, LoginView, LogoutView, SignUpView, UserProfileView, \
    ValidateTokenView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    # Server-Side Login and Logout for Web App
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # API Endpoints for Mobile App
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    path('api/signup/', SignUpView.as_view(), name='api-signup'),
    path('api/profile/', UserProfileView.as_view(), name='api-profile'),
    path('api/validate-token/', ValidateTokenView.as_view(), name='validate-token'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/verify-email/", , name="verify-email"),
]
