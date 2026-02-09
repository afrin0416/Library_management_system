from rest_framework import serializers
from .models import BorrowRecord
from books.serializers import BookSerializer
from members.serializers import MemberSerializer
from books.models import Book
from members.models import Member

class BorrowRecordSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), write_only=True, source='book'
    )
    member = MemberSerializer(read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), write_only=True, source='member'
    )

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'book_id', 'member', 'member_id', 'borrow_date', 'return_date']
