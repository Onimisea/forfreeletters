# accounts/urls.py
from django.urls import path

from . import views
from .views import VerifyEmailView

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("verify/<str:email>/", VerifyEmailView.as_view(), name="verify_email"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
