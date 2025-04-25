from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from restaurants.models import EmailVerification
import random



# Server-Side Login View for Web App
def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get('identifier')  # Can be email or username
        password = request.POST.get('password')

        # Use 'username' as the key since our custom backend accepts both username or email
        user = authenticate(request, username=identifier, password=password)

        if user:
            login(request, user)
            return redirect('restaurant:home')  # Redirect after login
        else:
            messages.error(request, "Invalid username/email or password.")
    return render(request, 'sign_in.html')


# Server-Side Logout View for Web App
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


# API Login View for Mobile App
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        identifier = request.data.get('identifier')  # Username or email
        password = request.data.get('password')

        # Use 'username' since our backend supports email or username
        user = authenticate(request, username=identifier, password=password)
        if user:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })
        return Response({'error': 'Invalid credentials'}, status=400)


# API Logout View for Mobile App
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the token
            return Response({'message': 'Successfully logged out'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)


# API Sign-Up View for Mobile App
class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')
        phone_number = data.get('phone_number')

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already in use'}, status=400)

        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'Phone number is already in use'}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number
        )

        # Generate verification code
        code = str(random.randint(100000, 999999))

        # Create email verification record
        EmailVerification.objects.create(
            user=user,
            code=code,
            is_verified=False
        )

        # Send verification email
        subject = "Verify your email - Seatify"
        html_message = render_to_string(
            "emails/verify_email.html",
            {"user": user, "code": code}
        )
        email_message = EmailMessage(subject, html_message, to=[email])
        email_message.content_subtype = "html"
        email_message.send()

        return Response({'message': 'User registered successfully. Please check your email for verification.'})


# API User Profile View for Mobile App
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })


class ValidateTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        return Response({
            "username": user.username
        })


@api_view(["POST"])
def verify_email_code(request):
    email = request.data.get("email")
    code = request.data.get("code")
    user = get_object_or_404(User, email=email)

    try:
        record = EmailVerification.objects.get(user=user)
        if record.code == code:
            record.is_verified = True
            record.save()
            return Response({"message": "Email verified successfully"}, status=200)
        else:
            return Response({"error": "Invalid verification code"}, status=400)
    except EmailVerification.DoesNotExist:
        return Response({"error": "Verification record not found"}, status=404)
