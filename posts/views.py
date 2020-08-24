from rest_framework import generics, permissions
from .models import Post
from .serializers import PostCreateSerializer, PostSerializer, PostUpdateSerializer
from .permissions import IsAuthor


# Create your views here.
class PostListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    permissions_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_serializer_context(self):
        context = super(PostDetailView, self).get_serializer_context()
        context.update({
            "request": self.request
        })
        return context


class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        # we need to pass the user so we can save with the associated user when we create a post.
        serializer.save(user=self.request.user)


class PostUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAuthor]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'


class PostDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAuthor]
    queryset = Post.objects.all()
    lookup_field = 'slug'