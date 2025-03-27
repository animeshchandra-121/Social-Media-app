from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return redirect('social:post')
    return render(request, 'navbar.html')

def login_page(request):
    page = 'login' 
    if request.user.is_authenticated:
        return redirect('social:post')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            print("Login successfully")
            return redirect('social:post')
        else:
            messages.error(request, "invalid login credentials")
        
    return render(request, "sign_up.html", {'page':page})

def logout_page(request):
    logout(request)
    return redirect('index')

def register(request):
    form = CustomUserCreationForm()
    context = {'form': form, 'page': 'register'}  # Add 'page' to context

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('social:post')  # Fix redirect
    
    return render(request, "sign_up.html", context)


