# blog/urls.py

from django.urls import path
from . import views  # Import your views

urlpatterns = [
  path("", views.index, name="index"),  # This links the root URL to the index view
]
