from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

class EmailBackend(BaseBackend):
    """
    Custom authentication backend to authenticate users using their email and password.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        """
        Rejects users with is_active=False.
        """
        return getattr(user, 'is_active', False)