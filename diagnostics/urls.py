from django.urls import path
from .views import predict_diagnosis
from .views import diagnose_crop
from . import views

urlpatterns = [
    path('', views.DiagnosisListCreateView.as_view(), name='diagnosis-list-create'),
    path('<int:pk>/', views.DiagnosisDetailView.as_view(), name='diagnosis-detail'),
    path('results/', views.DiagnosisResultListView.as_view(), name='diagnosis-results'),
     path('predict/', predict_diagnosis, name='predict-diagnosis'),
      path('predict/', diagnose_crop, name='crop-diagnosis'),

]
