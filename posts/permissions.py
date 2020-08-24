from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied # raising a permission when user isn't the owner.


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user