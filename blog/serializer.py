from rest_framework import serializers
from .models import Post, Comment


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    children = RecursiveSerializer(many=True)


    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comment
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
