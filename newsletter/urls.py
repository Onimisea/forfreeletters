from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='all-subscribers'),
    path("add", views.home, name='add-subscriber'),
]