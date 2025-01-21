from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameBackend(BaseBackend):
    """
    Custom authentication backend to authenticate users using their email or username and password.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Attempt to authenticate the user with either email or username.
        """
        try:
            # Check if the username is an email
            if '@' in username and '.' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        # Check the password and whether the user is active
        if user.check_password(password) and self.user_can_authenticate(user):
            return user

    def get_user(self, user_id):
        """
        Retrieve the user by ID.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        """
        Check if the user is active.
        """
        return getattr(user, 'is_active', False)