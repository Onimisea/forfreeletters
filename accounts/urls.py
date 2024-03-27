# accounts/urls.py
from django.urls import path

from . import views
from .views import VerifyEmailView

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("verify/<str:email>/", VerifyEmailView.as_view(), name="verify_email"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "forgotten-password/",
        views.ForgottenPasswordView.as_view(),
        name="forgotten_password",
    ),
    path(
        "reset-password/",
        views.ResetPasswordView.as_view(),
        name="reset_password",
    ),
    path("reset-done/", views.logout_view, name="reset_done"),
]
