from django.db import models
from django.conf import settings


class Disease(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    treatment = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Pest(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    treatment = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DiagnosticImage(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='diagnostic_images'
    )
    plant = models.ForeignKey(
        'farms.PlantInstance',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='diagnostic_images/')
    gps_location = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} by {self.farmer.username}"


class DiagnosisResult(models.Model):
    diagnostic_image = models.OneToOneField(
        DiagnosticImage,
        on_delete=models.CASCADE,
        related_name='result'
    )
    confidence_score = models.FloatField(default=0.0)
    raw_diagnostic_output = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return f"Diagnosis for Image {self.diagnostic_image.id}"


class DiseaseDiagnosis(models.Model):
    diagnosis_result = models.ForeignKey(DiagnosisResult, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    confidence = models.FloatField(default=0.0)

    class Meta:
        unique_together = ['diagnosis_result', 'disease']


class PestDiagnosis(models.Model):
    diagnosis_result = models.ForeignKey(DiagnosisResult, on_delete=models.CASCADE)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    confidence = models.FloatField(default=0.0)
    is_confirmed = models.BooleanField(default=False)
    confirmed_by = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='confirmed_diagnoses'
    )
    confirmed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['diagnosis_result', 'pest']
        verbose_name = "Pest Diagnosis"
        verbose_name_plural = "Pest Diagnoses"
        ordering = ['-id']
