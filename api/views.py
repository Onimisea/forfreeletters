from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import GenericTemplate
from main.serializers import GenericTemplateSerializer


class GenericTemplateList(APIView):
    def get(self, request):
        category = request.query_params.get("category")
        subcategory = request.query_params.get("subcategory")
        search_query = request.query_params.get("search")
        sort_by = request.query_params.get("sort_by", "-date_added")

        queryset = GenericTemplate.objects.all()

        if category and subcategory:
            queryset = queryset.filter(
                category=category, subcategory=subcategory
            )
        elif category:
            queryset = queryset.filter(category=category)
        elif subcategory:
            queryset = queryset.filter(subcategory=subcategory)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(category__icontains=search_query)
                | Q(subcategory__icontains=search_query)
            )

        queryset = queryset.order_by(sort_by)

        paginator = PageNumberPagination()
        paginator.page_size = 2

        result_page = paginator.paginate_queryset(queryset, request)
        serializer = GenericTemplateSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


class SubcategoriesList(APIView):
    def get(self, request, category=None):
        if category == "all":
            subcategories = GenericTemplate.objects.values_list(
                "subcategory", flat=True
            ).distinct()
        elif category:
            subcategories = (
                GenericTemplate.objects.filter(category=category)
                .values_list("subcategory", flat=True)
                .distinct()
            )
        else:
            return Response(
                {"error": "Category not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subcategories_list = list(subcategories)
        return Response(
            {"subcategories": subcategories_list}, status=status.HTTP_200_OK
        )
