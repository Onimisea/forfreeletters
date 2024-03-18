# accounts/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data
            user = form.save()
            # Extract the saved form data
            user_data = {
                'first_name': user.first_name,
                'email': user.email,
            }
            # Pass the form data as context to the success template
            return render(request, 'accounts/registration_success.html', {'user_data': user_data})
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    # Login logic here
    pass

def logout_view(request):
    # Logout logic here
    pass

