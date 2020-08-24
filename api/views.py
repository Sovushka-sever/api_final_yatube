from rest_framework import viewsets, filters
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment, Group, Follow, User
from .serializers import PostSerializer, \
    CommentSerializer, \
    GroupSerializer, \
    FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def get_queryset(self):
        post_id = self.kwargs.get('id')
        queryset = get_object_or_404(Post, pk=post_id).comments
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('id')
        )


class GroupView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(title=self.request.data.get('title'))


class FollowView(ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def perform_create(self, serializer):
        user = self.request.user
        following = get_object_or_404(
            User,
            username=self.request.POST.get('following')
        )
        serializer.save(user=user, following=following)
