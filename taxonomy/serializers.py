from rest_framework import serializers
from .models import Crop, Disease, Pest, DiseaseCrop, PestCrop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = '__all__'

class DiseaseCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseCrop
        fields = '__all__'

class PestCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestCrop
        fields = '__all__'
