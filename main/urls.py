from django.urls import path
from .views import HomeView, get_subcategories

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path('get-subcategories/<str:category>/', get_subcategories, name='get_subcategories'),
]