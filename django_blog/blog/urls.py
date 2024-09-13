from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, post_detail, comment_edit, comment_delete

urlpatterns = [
  # Home and post views
  path('', PostListView.as_view(), name='home'),
  path('posts/', PostListView.as_view(), name='posts'),
  path('post/<int:pk>/', views.post_detail, name='post-detail'),  # Updated to use function-based view for post detail
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

  # Comment-related views
  path('post/<int:post_pk>/comment/new/', views.post_detail, name='comment-create'),  # Comment creation happens in post_detail view
  path('comment/<int:pk>/edit/', comment_edit, name='comment-edit'),
  path('comment/<int:pk>/delete/', comment_delete, name='comment-delete'),

  # User Authentication URLs
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('register/', views.register, name='register'),
  path('profile/', views.profile, name='profile'),
]