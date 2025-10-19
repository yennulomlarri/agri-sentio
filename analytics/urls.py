from django.urls import path
from . import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def analytics_home(request):
    return Response({
        "message": "Analytics API is working!",
        "available_endpoints": {
            "summary": "/api/admin/analytics/summary/",
            "biosecurity": "/api/admin/analytics/biosecurity/"
        }
    })

urlpatterns = [
    path('', analytics_home, name='analytics_home'),
    path('summary/', views.summary_view, name='admin-summary'),
    path('biosecurity/', views.biosecurity_view, name='admin-biosecurity'),
]