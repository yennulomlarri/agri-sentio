# farms/serializers.py

from rest_framework import serializers
from .models import Farm

class FarmSerializer(serializers.ModelSerializer):
    """
    Serializer for the Farm model.
    Handles conversion between Farm objects and JSON for CRUD operations.
    """

    class Meta:
        model = Farm
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
