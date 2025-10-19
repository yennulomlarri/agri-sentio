from django.http import JsonResponse
from django.views import View

class FarmListCreateView(View):
    def get(self, request):
        return JsonResponse({"message": "List or create farms"})

class FarmDetailView(View):
    def get(self, request, pk):
        return JsonResponse({"message": f"Farm details for ID {pk}"})
