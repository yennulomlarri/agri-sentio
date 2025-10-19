from django.http import JsonResponse
from django.views import View

class DiagnosisListCreateView(View):
    def get(self, request):
        return JsonResponse({"message": "List or create diagnoses"})

class DiagnosisDetailView(View):
    def get(self, request, pk):
        return JsonResponse({"message": f"Diagnosis details for ID {pk}"})

class DiagnosisResultListView(View):
    def get(self, request):
        return JsonResponse({"message": "Diagnosis results list"})


from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.ml_utils import predict_disease
from django.core.files.storage import default_storage


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def predict_diagnosis(request):
    """
    POST /api/diagnostics/predict/
    Accepts an image upload and returns predicted disease and confidence.
    """
    if 'image' not in request.FILES:
        return Response({'error': 'No image file provided.'}, status=400)
    
    image = request.FILES['image'].read()
    result = predict_disease(image)
    return Response({
        "prediction": result['label'],
        "confidence": result['confidence']
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def diagnose_crop(request):
    """
    Upload an image and get an AI-based disease prediction.
    """
    if 'image' not in request.FILES:
        return Response({"error": "Please upload an image file."}, status=400)

    file = request.FILES['image']
    file_path = default_storage.save(file.name, file)
    result = predict_disease(file_path)

    return Response(result)
