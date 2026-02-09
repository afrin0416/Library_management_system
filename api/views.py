from rest_framework import viewsets
from authors.models import Author
from books.models import Book
from members.models import Member
from borrow.models import BorrowRecord
from authors.serializers import AuthorSerializer
from books.serializers import BookSerializer
from members.serializers import MemberSerializer
from borrow.serializers import BorrowRecordSerializer

# Create your views here.

# --------- Author ViewSet ----------
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# --------- Book ViewSet ----------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# --------- Member ViewSet ----------
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# --------- BorrowRecord ViewSet ----------
class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

