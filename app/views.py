from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm

def base(request):
    return render(request, "dashboard/home.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user, username, password)
        if user is not None:
            login(request, user)
            return redirect('base')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'authenticattion/login.html')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()
    
    return render(request, 'authenticattion/signup.html', {'form': form})

