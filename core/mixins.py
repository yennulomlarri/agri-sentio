# core/mixins.py

from rest_framework import status
from rest_framework.response import Response

class ConfirmMixin:
    """Reusable mixin for standardized update/delete confirmation messages."""

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        label = getattr(instance, "name", str(instance))
        instance.delete()
        return Response(
            {"detail": f"{label} deleted successfully."},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"detail": f"{self.basename.capitalize()} updated successfully.", "data": response.data},
            status=status.HTTP_200_OK
        )
