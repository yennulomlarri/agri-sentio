from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets
from .models import Farm
from .serializers import FarmSerializer
from core.mixins import ConfirmMixin


class FarmListCreateView(View):
    def get(self, request):
        return JsonResponse({"message": "List or create farms"})

class FarmDetailView(View):
    def get(self, request, pk):
        return JsonResponse({"message": f"Farm details for ID {pk}"})



class FarmViewSet(ConfirmMixin, viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
