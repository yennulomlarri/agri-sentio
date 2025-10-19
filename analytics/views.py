
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.db.models import Count
from farms.models import Farm
from diagnostics.models import DiagnosisResult

@api_view(['GET'])
@permission_classes([IsAdminUser])
def summary_view(request):
    """
    /api/admin/analytics/summary/
    Returns total users, total farms, and total diagnoses.
    """
    from accounts.models import User  # local import to avoid circular
    total_users = User.objects.count()
    total_farms = Farm.objects.count()
    total_diagnoses = DiagnosisResult.objects.count()

    data = {
        "total_users": total_users,
        "total_farms": total_farms,
        "total_diagnoses": total_diagnoses,
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def biosecurity_view(request):
    """
    /api/admin/analytics/biosecurity/
    Aggregates diagnosis data by REGION and DISTRICT.
    """
    # Use the Farm table because it stores REGION and DISTRICT
    region_summary = (
        Farm.objects.values('region', 'district')
        .annotate(total_diagnoses=Count('plant_instances__diagnoses'))
        .order_by('region', 'district')
    )

    return Response(region_summary)

