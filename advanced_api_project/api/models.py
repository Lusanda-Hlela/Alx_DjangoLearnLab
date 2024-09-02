from django.db import models

# Create your models here.

class Author(models.Model):
  # The Author model stores information about the authors of books.
  name = models.CharField(max_length=255)  # The author's name.

  def __str__(self):
    return self.name


class Book(models.Model):
  # The Book model stores information about books.
  title = models.CharField(max_length=255)  # The book's title.
  publication_year = models.IntegerField()  # The year the book was published.
  author = models.ForeignKey(
    Author, related_name="books", on_delete=models.CASCADE
  )  # Link to the author of the book.

  def __str__(self):
    return self.title
