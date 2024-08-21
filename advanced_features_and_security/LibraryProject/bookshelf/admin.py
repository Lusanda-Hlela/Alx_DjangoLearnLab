from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "publication_year")
  search_fields = ("title", "author")
  list_filter = ["publication_year"]  # Must be a list or tuple


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {"fields": ("username", "password")}),
    ("Personal info", {"fields": ("first_name", "last_name", "email")}),
    (
      "Permissions",
      {
        "fields": (
          "is_active",
          "is_staff",
          "is_superuser",
          "groups",
          "user_permissions",
        )
      },
    ),
    ("Important dates", {"fields": ("last_login", "date_joined")}),
    ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
  )
