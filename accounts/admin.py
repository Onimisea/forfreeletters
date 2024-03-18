from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'active_subscription', 'verified', 'date_joined', 'is_active')

# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
