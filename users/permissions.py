from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name="admin").exists()


class IsCurrentUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj
