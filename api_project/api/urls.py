from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

router = DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
  path(
      "api-token-auth/", obtain_auth_token, name="api_token_auth"
  ),  # Token retrieval endpoint
  path('books/', ListView.as_view(), name='book-list'),
  path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
  path('books/add/', CreateView.as_view(), name='book-create'),
  path('books/<int:pk>/edit/', UpdateView.as_view(), name='book-update'),
  path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
  path("", include(router.urls)),
]
