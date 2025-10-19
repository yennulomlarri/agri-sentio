from django.urls import path
from . import views

urlpatterns = [
    path('', views.FarmListCreateView.as_view(), name='farm-list-create'),
    path('<int:pk>/', views.FarmDetailView.as_view(), name='farm-detail'),
]
