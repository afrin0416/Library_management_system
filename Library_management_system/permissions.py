from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    """
    Only users in Librarian group can add/update/delete books.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Librarian').exists()
