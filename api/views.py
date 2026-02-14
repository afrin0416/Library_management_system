from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated   

from authors.models import Author
from books.models import Book
from members.models import Member
from borrow.models import BorrowRecord

from authors.serializers import AuthorSerializer
from books.serializers import BookSerializer
from members.serializers import MemberSerializer
from borrow.serializers import BorrowRecordSerializer


# --------- Author ViewSet ----------
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]   


# --------- Book ViewSet ----------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# --------- Member ViewSet ----------
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]


# --------- BorrowRecord ViewSet ----------
class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]
