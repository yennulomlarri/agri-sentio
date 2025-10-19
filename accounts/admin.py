from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, FarmerProfile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_farmer', 'is_admin', 'phone_number']
    list_filter = ['is_farmer', 'is_admin']
    fieldsets = UserAdmin.fieldsets + (
        ('Agri-Sentio Info', {'fields': ('is_farmer', 'is_admin', 'phone_number')}),
    )

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'region', 'district', 'date_joined']
    search_fields = ['user__username', 'region', 'district']