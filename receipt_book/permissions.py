from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Класс разрешения, проверяющий, является ли текущий пользователей
    владельцем объекта по полю user.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
