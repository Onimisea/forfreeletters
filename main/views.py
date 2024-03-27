from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from .models import GenericTemplate
from django.core.paginator import Paginator



class HomeView(ListView):
    template_name = 'home.html'
    model = GenericTemplate
    context_object_name = 'templates'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('s')
        category_filter = self.request.GET.get('category')
        subcategory_filter = self.request.GET.get('subcategory')

        queryset = GenericTemplate.objects.all()

        # Search functionality
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(subcategory__icontains=query))

        # Filtering by category and subcategory
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        if subcategory_filter:
            queryset = queryset.filter(subcategory=subcategory_filter)

        # Sorting
        sort_by = self.request.GET.get('sort_by', '-date_added')
        queryset = queryset.order_by(sort_by)

        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category_filter'] = self.request.GET.get('category')
    #     context['subcategory_filter'] = self.request.GET.get('subcategory')
    #     context['search_query'] = self.request.GET.get('s')
    #     context['sort_by'] = self.request.GET.get('sort_by', '-date_added')
    #     return context


class TemplatesView(ListView):
    model = GenericTemplate
    template_name = 'templates.html'
    context_object_name = 'templates'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('s')
        category_filter = self.request.GET.get('category')
        subcategory_filter = self.request.GET.get('subcategory')

        queryset = GenericTemplate.objects.all()

        # Search functionality
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(subcategory__icontains=query))

        # Filtering by category and subcategory
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        if subcategory_filter:
            queryset = queryset.filter(subcategory=subcategory_filter)

        # Sorting
        sort_by = self.request.GET.get('sort_by', '-date_added')
        queryset = queryset.order_by(sort_by)

        return 

class PrivacyPageView(ListView):
    model = GenericTemplate
    template_name = "privacy_page.html"
    context_object_name = "privacy_page"

    def get_queryset(self):
        pass




