from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: #request methods that do not change the database like the GET method
            return True
        else:
            return request.user.is_staff