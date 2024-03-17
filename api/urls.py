from django.urls import path
from .views import GenericTemplateList

urlpatterns = [
    path('generic-templates/', GenericTemplateList.as_view(), name='generic_template_list'),
]
