# accounts/views.py
from django.contrib.auth import get_user_model
from .forms import ResetPasswordForm
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.conf import settings
from .forms import UserRegistrationForm, UserLoginForm, ForgottenPasswordForm, ResetPasswordForm
from .models import CustomUser, PasswordResetToken
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


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
            messages.success(request, "Registration is successful. Please check your email to verify your account.")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user with provided email exists
            user = CustomUser.objects.filter(email=email).first()

            print(user)

            if user is not None:
                # Check if the user is verified
                if user.verified:
                    # Authenticate the user with provided email and password
                    authenticated_user = authenticate(
                        request, email=email, password=password)

                    if authenticated_user is not None:
                        login(request, authenticated_user)
                        messages.success(request, "Logged in successfully.")
                        return redirect('dashboard')
                    else:
                        messages.error(request, 'Invalid email or password.')
                else:
                    messages.error(
                        request, 'Your account is not verified. Please check your email to verify your account.')
            else:
                # If user does not exist
                messages.error(request, 'No user exists with this email.')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
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


class ForgottenPasswordView(View):
    template_name = "accounts/forgotten-password.html"

    def get(self, request):
        form = ForgottenPasswordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ForgottenPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()

            if user is not None:
                # Generate token and save it in the database
                token = default_token_generator.make_token(user)
                PasswordResetToken.objects.create(user=user, token=token)

                reset_link = request.build_absolute_uri(
                    '/reset-password/') + f'?token={token}'

                try:
                    subject = "Password Reset Link"
                    context = {
                        "first_name": user.first_name,
                        "reset_link": reset_link,
                    }
                    html_message = render_to_string(
                        "emails/password_reset_email.html", context
                    )

                    email = EmailMessage(
                        subject, html_message, settings.EMAIL_HOST_USER, [
                            user.email]
                    )
                    email.content_subtype = "html"
                    email.send()

                    messages.success(
                        request, "Password reset link sent successfully. Please check your email.")
                except Exception as e:
                    # Handle email sending failure
                    print(e)
                    messages.error(request, e)
            else:
                form.add_error('email', 'No user exists with this email.')
        return render(request, self.template_name, {'form': form})


class ResetPasswordView(View):
    template_name = "accounts/reset-password.html"

    def get(self, request):
        form = ResetPasswordForm()

        # Get the token from the URL query parameters
        token = request.GET.get('token')

        if not token:
            messages.error(request, "Password reset token not found!")

            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Get the token from the URL query parameters
            token = request.GET.get('token')

            if not token:
                messages.error(request, "Password reset token not found!")
                return render(request, self.template_name, {'form': form})

            # Verify that the passwords match
            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match.')
                return render(request, self.template_name, {'form': form})

            try:
                user_token = PasswordResetToken.objects.get(token=token)
                user = user_token.user

                # Change the user's password
                user.set_password(password)
                user.save()

                # Delete the token from the database
                user_token.delete()

                messages.success(
                    request, "Password reset successful. Please login with your new password.")
                return redirect('login')
            except PasswordResetToken.DoesNotExist:
                messages.error(
                    request, "Invalid password reset token, please try again.")
                return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})
