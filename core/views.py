from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health_check(request):
    """
    Simple endpoint to confirm the API is operational.
    """
    return Response({
        "status": "ok",
        "message": "Agri-Sentio API is running smoothly."
    })


@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "ok",
        "message": "Agri-Sentio API is running smoothly."
    })
