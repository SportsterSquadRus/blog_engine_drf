from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'body',)


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('draft',)
