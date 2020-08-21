from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Comment, Post, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False
    )
    author_name = serializers.CharField(
        source='author.get_full_name',
        required=False
    )

    class Meta:
        fields = ('id', 'text', 'image', 'author', 'author_name', 'pub_date')
        model = Post
        read_only_fields = ['author', 'pub_date']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False
    )
    author_name = serializers.CharField(
        source='author.get_full_name',
        required=False
    )

    class Meta:
        fields = ('id', 'text', 'author', 'author_name', 'created', 'post')
        model = Comment
        read_only_fields = ['author', 'created']


class FollowSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow
