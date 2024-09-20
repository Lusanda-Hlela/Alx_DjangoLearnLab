from rest_framework import viewsets, generics
from rest_framework import permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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
