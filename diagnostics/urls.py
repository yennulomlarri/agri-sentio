from django.urls import path
from .views import (
    DiagnosisListCreateView,
    DiagnosisRetrieveUpdateDeleteView,
    DiagnosisDetailView,
    DiagnosisResultListView,
    predict_diagnosis,
    diagnose_crop,
    confirm_diagnosis,
)

urlpatterns = [
    path('', DiagnosisListCreateView.as_view(), name='diagnosis-list-create'),
    path('results/', DiagnosisResultListView.as_view(), name='diagnosis-results'),
    path('<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis-detail'),
    path('<int:pk>/edit/', DiagnosisRetrieveUpdateDeleteView.as_view(), name='diagnosis-edit'),
    path('predict/', predict_diagnosis, name='predict-diagnosis'),
    path('diagnose/', diagnose_crop, name='diagnose-crop'),
    path('<int:pk>/confirm/', confirm_diagnosis, name='confirm-diagnosis'),
]
