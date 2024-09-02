from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
  # The BookSerializer serializes the Book model, including validation for the publication year.
  class Meta:
    model = Book
    fields = "__all__"

  def validate_publication_year(self, value):
    # Ensure the publication year is not in the future.
    if value > datetime.date.today().year:
      raise serializers.ValidationError(
        "Publication year cannot be in the future."
      )
    return value

class AuthorSerializer(serializers.ModelSerializer):
  # The AuthorSerializer serializes the Author model, including nested serialization of related books.
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = ["name", "books"]