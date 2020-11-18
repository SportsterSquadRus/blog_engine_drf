from rest_framework import serializers
from .models import Post, Comment, Like, Tag
from .utils import banned_tags_check


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagSerializer(serializers.Serializer):
    tag_title = serializers.CharField(max_length=200)


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Like
        fields = ('user', )


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
    likes = LikeSerializer(many=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comment
        fields = ('author', 'date_pub', 'total_likes', 'likes', 'children')


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('author', 'published','title', 'body', 'total_likes', 'tags', 'likes', 'comments')


class PostCreateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'draft', 'tags')

    def create(self, validated_data):
        print(validated_data)
        tags = validated_data.pop('tags')

        post = Post.objects.create(**validated_data)
        for tag in tags:
            if banned_tags_check(tag['tag_title']):
                tag_object, created = Tag.objects.get_or_create(tag_title=tag['tag_title'])
                post.tags.add(tag_object)
        return post
#   {"title": "post3", "body": "lala<<hr />lolo", "author":1, "draft": false, "tags": [ {"tag_title": "tag2"}, {"tag_title": "tag4"} ]}
