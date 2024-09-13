from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
  path('', PostListView.as_view(), name='home'),
  path('posts/', PostListView.as_view(), name='posts'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

  # User Authentication URLs
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('register/', views.register, name='register'),
  path('profile/', views.profile, name='profile'),
]