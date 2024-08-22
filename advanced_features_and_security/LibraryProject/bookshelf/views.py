from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
  # Logic for editing a book
  return render(request, "bookshelf/edit_book.html")
