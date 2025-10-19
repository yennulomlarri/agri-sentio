from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CropViewSet, DiseaseViewSet, PestViewSet,
    DiseaseCropViewSet, PestCropViewSet
)

router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'diseases', DiseaseViewSet)
router.register(r'pests', PestViewSet)
router.register(r'disease-crops', DiseaseCropViewSet)
router.register(r'pest-crops', PestCropViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
