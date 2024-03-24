# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from .forms import UserRegistrationForm, UserLoginForm
from .models import CustomUser


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data
            user = form.save()
            # Extract the saved form data
            user_data = {
                "first_name": user.first_name,
                "email": user.email,
            }
            # Pass the form data as context to the success template
            return render(
                request,
                "accounts/registration_success.html",
                {"user_data": user_data},
            )
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                # Replace 'index' with your desired URL after login
                return redirect('dashboard')
            else:
                # Invalid login
                form.add_error(None, 'Invalid email or password.')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


class VerifyEmailView(View):
    template_name = "accounts/verify_email.html"  # Updated template name

    def get(self, request, email):
        user = get_object_or_404(CustomUser, email=email)

        if user.verified:
            message = "This account has already been verified."
        else:
            user.verified = True
            user.save()
            message = "Account verified successfully."

        return render(request, self.template_name, {"message": message})
