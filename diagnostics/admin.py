from django.contrib import admin
from .models import Disease, Pest, DiagnosticImage, DiagnosisResult, DiseaseDiagnosis, PestDiagnosis

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name']
    search_fields = ['name', 'scientific_name']

@admin.register(Pest)
class PestAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name']
    search_fields = ['name', 'scientific_name']

@admin.register(DiagnosticImage)
class DiagnosticImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'farmer', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['farmer__username']

@admin.register(DiagnosisResult)
class DiagnosisResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'diagnostic_image', 'confidence_score', 'is_urgent', 'created_at']
    list_filter = ['is_urgent', 'created_at']

admin.site.register(DiseaseDiagnosis)
admin.site.register(PestDiagnosis)