from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import GenericTemplate
from main.serializers import GenericTemplateSerializer
from rest_framework.pagination import PageNumberPagination

class GenericTemplateList(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        subcategory = request.query_params.get('subcategory')
        search_query = request.query_params.get('search')
        sort_by = request.query_params.get('sort_by', '-date_added')

        queryset = GenericTemplate.objects.all()

        if category and subcategory:
            queryset = queryset.filter(category=category, subcategory=subcategory)
        elif category:
            queryset = queryset.filter(category=category)
        elif subcategory:
            queryset = queryset.filter(subcategory=subcategory)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(category__icontains=search_query) |
                Q(subcategory__icontains=search_query)
            )

        queryset = queryset.order_by(sort_by)
        
        paginator = PageNumberPagination()
        paginator.page_size = 2
        
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = GenericTemplateSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)
