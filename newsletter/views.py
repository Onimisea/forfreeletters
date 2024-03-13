from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page! All subscribers are listed here.")

def add_subscriber(request):
    return HttpResponse("Add a new subscriber here.")
