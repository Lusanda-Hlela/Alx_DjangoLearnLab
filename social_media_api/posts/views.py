from rest_framework import viewsets, generics, status
from rest_framework import permissions
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

# Post view for handling posts CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comment view for handling comments CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# View for showing the feed with posts from followed users
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the users that the current user is following
        following_users = request.user.following.all()

        # Fetch posts from the users that the current user is following, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

        # Serialize the posts and return them
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

# View to handle liking a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if the user has already liked the post
        if Like.objects.filter(post=post, user=user).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a like instance
        Like.objects.create(post=post, user=user)
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

# View to handle unliking a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like instance
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
