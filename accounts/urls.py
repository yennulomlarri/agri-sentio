from django.urls import path
from . import views
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.urls import path
from . import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Add a simple view for the base endpoint
@api_view(['GET'])
def accounts_home(request):
    return Response({
        "message": "Accounts API is working!",
        "available_endpoints": {
            "register": "/api/accounts/register/",
            "login": "/api/accounts/login/", 
            "profile": "/api/accounts/profile/"
        }
    })

urlpatterns = [
    # Base endpoint
    path('', accounts_home, name='accounts_home'),
    
    # Authentication - your existing endpoints
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]