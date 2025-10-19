# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     is_farmer = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     phone_number = models.CharField(max_length=15, blank=True)
    
#     def __str__(self):
#         return self.username

# class FarmerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     region = models.CharField(max_length=100)
#     district = models.CharField(max_length=100)
#     gps_centroid = models.CharField(max_length=100, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.user.username} - {self.region}"
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_farmer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.username

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    gps_centroid = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.region}"