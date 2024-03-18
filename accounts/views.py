from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    # Login logic here
    pass

def logout_view(request):
    # Logout logic here
    pass

def register_view(request):
    # Registration logic here
    pass
