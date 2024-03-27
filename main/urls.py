from django.urls import path
from .views import HomeView, TemplatesView, PrivacyPageView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("templates/", TemplatesView.as_view(), name='templates'),
    path("privacy/", PrivacyPageView.as_view(), name='privacy_page'),
]