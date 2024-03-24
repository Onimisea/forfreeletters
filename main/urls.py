from django.urls import path

from .views import HomeView, TemplatesView, DashboardView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("templates/", TemplatesView.as_view(), name="templates"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
