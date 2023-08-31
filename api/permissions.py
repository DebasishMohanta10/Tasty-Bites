from rest_framework import permissions

class ManagerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Manager").exists() or request.user.is_superuser:
            return True
        return False
