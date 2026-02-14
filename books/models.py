# books/models.py
from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=50)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
