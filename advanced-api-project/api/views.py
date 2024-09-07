from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# ListView - Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# DetailView - Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# CreateView - Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic before saving the book (if needed)
        serializer.save()


# UpdateView - Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic before updating the book (if needed)
        serializer.save()


# DeleteView - Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# AuthorListView - Retrieve all authors
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# AuthorDetailView - Retrieve a single author by ID
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
