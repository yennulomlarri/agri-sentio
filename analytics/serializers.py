from rest_framework import serializers


class SummarySerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    total_farms = serializers.IntegerField()
    total_diagnoses = serializers.IntegerField()


class BiosecuritySerializer(serializers.Serializer):
    region = serializers.CharField()
    district = serializers.CharField()
    total_diagnoses = serializers.IntegerField()
