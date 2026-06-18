from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'index.html')


def login_page(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def register_page(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'accounts/register.html')
def logout_page(request):
    logout(request)
    return redirect('login')