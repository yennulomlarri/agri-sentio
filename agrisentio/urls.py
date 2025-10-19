from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# Homepage view
def home(request):
    return HttpResponse("""
    <h1>Agri-Sentio Backend API</h1>
    <p>Server is running successfully!</p>
    <ul>
        <li><a href="/api/docs/">API Documentation</a></li>
        <li><a href="/admin/">Django Admin</a></li>
        <li><a href="/api/accounts/">Accounts API</a></li>
        <li><a href="/api/admin/analytics/">Analytics API</a></li>
    </ul>
    """)

urlpatterns = [
    # Homepage
    path('', home, name='home'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/accounts/', include('accounts.urls')),
    path('api/farms/', include('farms.urls')),
    path('api/diagnostics/', include('diagnostics.urls')),
    path('api/admin/analytics/', include('analytics.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/taxonomy/', include('taxonomy.urls')),
    path('api/core/', include('core.urls')),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


