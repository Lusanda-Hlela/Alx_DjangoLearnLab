from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ListView: Retrieve all books
class ListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

# DetailView: Retrieve a single book by ID
class DetailView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

# CreateView: Add a new book
class CreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# UpdateView: Modify an existing book
class UpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# DeleteView: Remove a book
class DeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
