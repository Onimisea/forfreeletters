from django.urls import path
from .views import HomeView, TemplatesView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("templates/", TemplatesView.as_view(), name='templates'),
]