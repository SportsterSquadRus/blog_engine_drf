from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('author', 'body', 'date_pub')



class PostListSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True)


    class Meta:
        model = Post
        fields = '__all__'