from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView  # Import FeedView

# Set up a router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# Define the URL patterns
urlpatterns = [
  path('', include(router.urls)),  # Routes for posts and comments
  path('feed/', FeedView.as_view(), name='feed'),  # Add feed route
]
