from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow owners to edit, others read-only."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'owner') and obj.owner == request.user


from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Allows full access to admin users, read-only for others.
    """
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user and request.user.is_staff


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
