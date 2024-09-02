from rest_framework import serializers
from .models import Book
import datetime


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = "__all__"

  def validate_publication_year(self, value):
    if value > datetime.date.today().year:
      raise serializers.ValidationError(
        "The publication year cannot be in the future."
      )
    return value
