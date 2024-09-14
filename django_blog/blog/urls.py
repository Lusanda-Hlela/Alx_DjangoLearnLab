from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # Home and post views
    path("", PostListView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="posts"),
    path(
        "post/<int:pk>/", views.post_detail, name="post-detail"
    ),  # Using function-based view for post detail
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # Comment-related views
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),  # Updated to match the required URL pattern
    path(
        "comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-edit"
    ),  # Updated the path for consistency
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
    # User Authentication URLs
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
