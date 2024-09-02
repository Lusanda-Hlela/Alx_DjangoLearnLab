from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAdminOrReadOnly]  # Only authenticated users can access


# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
