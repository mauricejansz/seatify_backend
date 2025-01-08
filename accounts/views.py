from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)  # Use email instead of username
        if user:
            login(request, user)
            return redirect('restaurant:home')  # Redirect after login
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'sign_in.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')
