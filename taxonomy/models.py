from django.db import models

class Crop(models.Model):
    """
    Represents a crop (e.g. Maize, Cocoa, Tomato).
    """
    name = models.CharField(max_length=100, unique=True)
    scientific_name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    """
    Represents a crop disease.
    """
    name = models.CharField(max_length=100, unique=True)
    cause = models.CharField(max_length=200, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Pest(models.Model):
    """
    Represents a crop pest.
    """
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class DiseaseCrop(models.Model):
    """
    Junction table linking Disease <-> Crop.
    """
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name="disease_links")
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name="crop_links")

    class Meta:
        unique_together = ('crop', 'disease')

    def __str__(self):
        return f"{self.disease.name} affects {self.crop.name}"


class PestCrop(models.Model):
    """
    Junction table linking Pest <-> Crop.
    """
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name="pest_links")
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE, related_name="crop_links")

    class Meta:
        unique_together = ('crop', 'pest')

    def __str__(self):
        return f"{self.pest.name} attacks {self.crop.name}"
