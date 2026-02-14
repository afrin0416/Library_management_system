from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets   
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from Library_management_system.permissions import IsLibrarian  


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [IsAuthenticated()]
        return [IsLibrarian()]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def borrow(self, request, pk=None):
        book = self.get_object()
        if book.is_borrowed:
            return Response({"error": "Already borrowed"})
        book.is_borrowed = True
        book.borrowed_by = request.user
        book.save()
        return Response({"status": "Borrowed successfully"})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def return_book(self, request, pk=None):
        book = self.get_object()
        if book.borrowed_by != request.user:
            return Response({"error": "You didn't borrow this book"})
        book.is_borrowed = False
        book.borrowed_by = None
        book.save()
        return Response({"status": "Returned successfully"})
