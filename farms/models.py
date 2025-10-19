from django.db import models
from django.conf import settings

class Crop(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Farm(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farms')
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    gps_centroid = models.CharField(max_length=100, blank=True)
    size_acres = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.region}"

class PlantInstance(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='plants')
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = models.CharField(max_length=100, blank=True)
    planting_date = models.DateField(null=True, blank=True)
    health_status = models.CharField(max_length=50, default='HEALTHY')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop.name} - {self.farm.name}"