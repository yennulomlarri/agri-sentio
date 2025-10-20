from rest_framework import serializers
from .models import DiagnosisResult
from farms.models import Farm
from taxonomy.models import Disease


class DiagnosisResultSerializer(serializers.ModelSerializer):
    """
    Serializer for the DiagnosisResult model.
    Converts model data to/from JSON for the API.
    """

    farm_name = serializers.CharField(source='farm.name', read_only=True)
    disease_name = serializers.CharField(source='disease.name', read_only=True)

    class Meta:
        model = DiagnosisResult
        fields = [
            'id',
            'farm',
            'farm_name',
            'image',
            'prediction_label',
            'confidence',
            'disease',
            'disease_name',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class FarmMinimalSerializer(serializers.ModelSerializer):
    """
    Minimal serializer to display related Farm info in analytics or summary endpoints.
    """
    class Meta:
        model = Farm
        fields = ['id', 'name', 'region', 'district']


class DiseaseMinimalSerializer(serializers.ModelSerializer):
    """
    Minimal serializer to display related Disease info.
    """
    class Meta:
        model = Disease
        fields = ['id', 'name', 'type']


class DiagnosisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisResult
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'confirmed_by', 'confirmed_at']
