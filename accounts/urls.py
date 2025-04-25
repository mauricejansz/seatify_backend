from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    # Server-Side Login and Logout for Web App
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.manage_users, name='manage_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),

    # API Endpoints for Mobile App
    path('api/login/', views.LoginView.as_view(), name='api-login'),
    path('api/logout/', views.LogoutView.as_view(), name='api-logout'),
    path('api/signup/', views.SignUpView.as_view(), name='api-signup'),
    path('api/profile/', views.UserProfileView.as_view(), name='api-profile'),
    path('api/validate-token/', views.ValidateTokenView.as_view(), name='validate-token'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/verify_email/", views.verify_email_code, name="verify_email_code"),
    path("api/update_profile/", views.update_profile, name="update_profile"),
]
