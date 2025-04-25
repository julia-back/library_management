from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Класс разрешения, проверяет, состоит ли пользователь в
    группе администраторов.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name="admin").exists()


class IsCurrentUser(BasePermission):
    """
    Класс разрешения, проверяет, является ли получаемый объект текущм
    авторизованным пользователем.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj
