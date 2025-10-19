from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """Abstract base model for shared fields."""
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id})"
