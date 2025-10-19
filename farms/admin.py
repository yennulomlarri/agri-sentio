from django.contrib import admin
from .models import Crop, Farm, PlantInstance

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name']
    search_fields = ['name', 'scientific_name']

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'farmer', 'region', 'district', 'created_at']
    list_filter = ['region', 'district']
    search_fields = ['name', 'farmer__username']

@admin.register(PlantInstance)
class PlantInstanceAdmin(admin.ModelAdmin):
    list_display = ['crop', 'farm', 'health_status', 'created_at']
    list_filter = ['health_status', 'crop__name']
    search_fields = ['farm__name', 'variety']