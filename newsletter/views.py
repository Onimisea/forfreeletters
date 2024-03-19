from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber

def home(request):
    return HttpResponse("Welcome to the home page! All subscribers are listed here.")

def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            return HttpResponse('You are already subscribed!')
        else:
            Subscriber.objects.create(email=email)
            return HttpResponse('Thank you for subscribing!')
    else:
        # Handle GET request or any other method if needed
        return HttpResponse('Invalid request method')
