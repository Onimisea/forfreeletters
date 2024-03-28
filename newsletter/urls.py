from django.urls import path

from . import views

app_name = "newsletter"

urlpatterns = [
    path("", views.home, name="all-subscribers"),
    path("add/", views.add_subscriber, name="add-subscriber"),
]
