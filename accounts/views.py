from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def logout_view(request):
    logout(request)
    return redirect('accounts:login')