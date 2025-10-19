from rest_framework import viewsets
from .models import Crop, Disease, Pest, DiseaseCrop, PestCrop
from .serializers import (
    CropSerializer, DiseaseSerializer, PestSerializer,
    DiseaseCropSerializer, PestCropSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PestViewSet(viewsets.ModelViewSet):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DiseaseCropViewSet(viewsets.ModelViewSet):
    queryset = DiseaseCrop.objects.all()
    serializer_class = DiseaseCropSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PestCropViewSet(viewsets.ModelViewSet):
    queryset = PestCrop.objects.all()
    serializer_class = PestCropSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
