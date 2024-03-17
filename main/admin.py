from django.contrib import admin
from .models import GenericTemplate

# Register your models here.


class GenericTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'category', 'date_added', 'date_updated')
    list_filter = ('subcategory', 'category', 'date_added', 'date_updated')
    search_fields = ('name', 'subcategory', 'category')
    ordering = ('-date_added',)

admin.site.register(GenericTemplate, GenericTemplateAdmin)
