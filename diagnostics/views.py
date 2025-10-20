from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.utils import timezone
from rest_framework.permissions import IsAdminUser

from .models import DiagnosisResult
from .serializers import DiagnosisResultSerializer
from core.ml_utils import predict_disease


# -------------------------
# CRUD Views
# -------------------------

class DiagnosisListCreateView(generics.ListCreateAPIView):
    """GET → List all diagnosis results | POST → Create a new diagnosis"""
    queryset = DiagnosisResult.objects.all().order_by('-created_at')
    serializer_class = DiagnosisResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiagnosisRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """GET → Retrieve one diagnosis | PUT/PATCH → Update | DELETE → Remove"""
    queryset = DiagnosisResult.objects.all()
    serializer_class = DiagnosisResultSerializer
    permission_classes = [permissions.AllowAny]



# 🆕 Added — Detail view (used in URLs)
class DiagnosisDetailView(generics.RetrieveAPIView):
    """GET → Retrieve details of a specific diagnosis"""
    queryset = DiagnosisResult.objects.all()
    serializer_class = DiagnosisResultSerializer
    permission_classes = [permissions.IsAuthenticated]


# 🆕 Added — List view for results (used in URLs)
class DiagnosisResultListView(generics.ListAPIView):
    """GET → List all stored diagnosis results"""
    queryset = DiagnosisResult.objects.all().order_by('-created_at')
    serializer_class = DiagnosisResultSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------------
# AI Prediction Endpoints
# -------------------------

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def predict_diagnosis(request):
    """POST /api/diagnostics/predict/ → AI model predicts disease from image"""
    if 'image' not in request.FILES:
        return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

    file = request.FILES['image']
    file_path = default_storage.save(file.name, file)
    result = predict_disease(file_path)

    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def diagnose_crop(request):
    """POST /api/diagnostics/diagnose/ → Alternative crop diagnosis endpoint"""
    if 'image' not in request.FILES:
        return Response({"error": "Please upload an image file."}, status=status.HTTP_400_BAD_REQUEST)

    file = request.FILES['image']
    file_path = default_storage.save(file.name, file)
    result = predict_disease(file_path)

    return Response(result, status=status.HTTP_200_OK)


# -------------------------
# Admin: Confirm Diagnosis
# -------------------------

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def confirm_diagnosis(request, pk):
    """PATCH /api/diagnostics/<id>/confirm/ → Admin confirms a diagnosis"""
    try:
        diagnosis = DiagnosisResult.objects.get(pk=pk)
    except DiagnosisResult.DoesNotExist:
        return Response({"error": "Diagnosis not found"}, status=status.HTTP_404_NOT_FOUND)

    if getattr(diagnosis, 'is_confirmed', False):
        return Response({"message": "This diagnosis has already been confirmed."}, status=status.HTTP_200_OK)

    diagnosis.is_confirmed = True
    diagnosis.confirmed_by = request.user
    diagnosis.confirmed_at = timezone.now()
    diagnosis.save()

    serializer = DiagnosisResultSerializer(diagnosis)
    return Response(serializer.data, status=status.HTTP_200_OK)
