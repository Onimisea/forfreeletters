from django.urls import path
from .views import GenericTemplateList, SubcategoriesList

urlpatterns = [
    path('generic-templates/', GenericTemplateList.as_view(), name='generic_template_list'),
    path('get-subcategories/<str:category>/', SubcategoriesList.as_view(), name='get_subcategories'),
]
