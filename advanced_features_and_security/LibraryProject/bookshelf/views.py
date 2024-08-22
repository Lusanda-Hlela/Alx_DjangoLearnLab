from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book  # Import your Book model


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
  # Logic for editing a book
  return render(request, "bookshelf/edit_book.html")

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
  # Logic for displaying a list of books
  books = Book.objects.all()  # Fetch all books from the database
  return render(request, "bookshelf/book_list.html", {"books": books})