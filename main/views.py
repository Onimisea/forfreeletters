from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GenericTemplate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


class HomeView(ListView):
    template_name = "home.html"
    model = GenericTemplate
    context_object_name = "templates"
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get("s")
        category_filter = self.request.GET.get("category")
        subcategory_filter = self.request.GET.get("subcategory")

        queryset = GenericTemplate.objects.all()

        # Search functionality
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
                | Q(category__icontains=query)
                | Q(subcategory__icontains=query)
            )

        # Filtering by category and subcategory
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        if subcategory_filter:
            queryset = queryset.filter(subcategory=subcategory_filter)

        # Sorting
        sort_by = self.request.GET.get("sort_by", "-date_added")
        queryset = queryset.order_by(sort_by)

        return queryset


class TemplatesView(ListView):
    model = GenericTemplate
    template_name = "templates.html"
    context_object_name = "templates"
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get("s")
        category_filter = self.request.GET.get("category")
        subcategory_filter = self.request.GET.get("subcategory")

        queryset = GenericTemplate.objects.all()

        # Search functionality
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
                | Q(category__icontains=query)
                | Q(subcategory__icontains=query)
            )

        # Filtering by category and subcategory
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        if subcategory_filter:
            queryset = queryset.filter(subcategory=subcategory_filter)

        # Sorting
        sort_by = self.request.GET.get("sort_by", "-date_added")
        queryset = queryset.order_by(sort_by)

        return queryset


class ContactsView(View):
    template_name = "contacts.html"
    context_object_name = "contacts"

    def get(self, request):
        return render(request, self.template_name)


class DashboardView(LoginRequiredMixin, ListView):
    model = GenericTemplate
    template_name = "dashboard.html"
    context_object_name = "dashboard"
    paginate_by = 12
    login_url = reverse_lazy("login")  # Specify the login URL

    def get_queryset(self):
        query = self.request.GET.get("s")
        category_filter = self.request.GET.get("category")
        subcategory_filter = self.request.GET.get("subcategory")

        queryset = GenericTemplate.objects.all()

        # Search functionality
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
                | Q(category__icontains=query)
                | Q(subcategory__icontains=query)
            )

        # Filtering by category and subcategory
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        if subcategory_filter:
            queryset = queryset.filter(subcategory=subcategory_filter)

        # Sorting
        sort_by = self.request.GET.get("sort_by", "-date_added")
        queryset = queryset.order_by(sort_by)

        return queryset
