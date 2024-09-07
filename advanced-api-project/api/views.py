from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [
    IsAuthenticatedOrReadOnly
  ] # Allows read for unauthenticated users

  def perform_create(self, serializer):
    # Custom logic before saving the book (if needed)
    serializer.save()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [
    IsAuthenticatedOrReadOnly
  ] # Allows read for unauthenticated users

  def perform_update(self, serializer):
    # Custom logic before updating the book (if needed)
    serializer.save()

  def perform_destroy(self, instance):
    # Custom logic before deleting the book (if needed)
    instance.delete()


class BookCreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]  # Only authenticated users can create

  def perform_create(self, serializer):
    # Custom logic before saving the book (if needed)
    serializer.save()


class BookUpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]  # Only authenticated users can update

  def perform_update(self, serializer):
    # Custom logic before updating the book (if needed)
    serializer.save()


class BookDeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]  # Only authenticated users can delete


class AuthorListView(generics.ListCreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  permission_classes = [
    IsAuthenticatedOrReadOnly
  ] # Allows read for unauthenticated users

  def perform_create(self, serializer):
    # Custom logic before saving the author (if needed)
    serializer.save()


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  permission_classes = [
    IsAuthenticatedOrReadOnly
  ]  # Allows read for unauthenticated users

  def perform_update(self, serializer):
    # Custom logic before updating the author (if needed)
    serializer.save()

  def perform_destroy(self, instance):
    # Custom logic before deleting the author (if needed)
    instance.delete()
