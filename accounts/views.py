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
from .models import EmailVerification
import random
import json
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from .forms import UserForm
import random
import string

def super_admin_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.role == 'super_admin')(view_func)

@super_admin_required
def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Auto-generate password
            password = generate_secure_password()
            user.set_password(password)
            user.save()

            if user.role == 'manager':

                # Send invitation email
                subject = "You're invited to Seatify!"
                html_message = render_to_string(
                    "emails/invite_manager.html",
                    {
                        "user": user,
                        "password": password,
                        "login_url": f"{settings.BACKEND_URL}/accounts/login/",
                    }
                )
                email = EmailMessage(subject, html_message, to=[user.email])
                email.content_subtype = "html"
                email.send()

                return redirect('accounts:manage_users')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:manage_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@require_POST
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('accounts:manage_users')

def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        user = authenticate(request, username=identifier, password=password)

        if user:
            login(request, user)
            return redirect('restaurant:home')
        else:
            messages.error(request, "Invalid username/email or password.")
    return render(request, 'sign_in.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        identifier = request.data.get('identifier')
        password = request.data.get('password')

        user = authenticate(request, username=identifier, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone_number': user.phone_number,
                    'email': user.email
                }
            })
        return Response({'error': 'Invalid credentials'}, status=400)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)


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

        code = str(random.randint(100000, 999999))

        EmailVerification.objects.create(
            user=user,
            code=code,
            is_verified=False
        )

        subject = "Verify your email - Seatify"
        html_message = render_to_string(
            "emails/verify_email.html",
            {"user": user, "code": code}
        )
        email_message = EmailMessage(subject, html_message, to=[email])
        email_message.content_subtype = "html"
        email_message.send()

        return Response({'message': 'User registered successfully. Please check your email for verification.'})


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

@csrf_exempt
def verify_email_code(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        code = data.get("code")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    user = get_object_or_404(User, email=email)

    try:
        record = EmailVerification.objects.get(user=user)
        if record.code == code:
            record.is_verified = True
            record.save()
            return JsonResponse({"message": "Email verified successfully"}, status=200)
        else:
            return JsonResponse({"error": "Invalid verification code"}, status=400)
    except EmailVerification.DoesNotExist:
        return JsonResponse({"error": "Verification record not found"}, status=404)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    data = request.data
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.username = data.get('username', user.username)
    user.phone_number = data.get('phone_number', user.phone_number)
    user.save()
    return Response({"message": "Profile updated successfully"}, status=200)

def generate_secure_password(length=12):
    chars = string.ascii_letters + string.digits
    symbols = "!@#$%^&*()-_=+"
    password = ''.join(random.choice(chars) for _ in range(length - 2))
    password += random.choice(symbols)
    password += random.choice(symbols)
    return ''.join(random.sample(password, len(password)))  # Shuffle it
