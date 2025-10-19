from django.contrib import admin
from .models import Crop, Disease, Pest, DiseaseCrop, PestCrop

admin.site.register(Crop)
admin.site.register(Disease)
admin.site.register(Pest)
admin.site.register(DiseaseCrop)
admin.site.register(PestCrop)
