from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostListSerializer, PostSerializer, CommentCreateSerializer, PostCreateSerializer
from .models import Post, Comment
from django.utils import timezone


class PostsListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(draft=False)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetialView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk, draft=False)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostCreateView(APIView):
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)

        if serializer.is_valid():
            new_post = serializer.save()
            if '<hr />' in new_post.body:
                new_post.truncate = len(
                    new_post.body[:new_post.body.find('<hr />')])
            else:
                new_post.truncate = 50

        if new_post.draft == False:
            new_post.published = timezone.now()
        new_post.save()

        return Response(status=201)


class PostUpdateView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostCreateSerializer(data=request.data, instance=post)

        if serializer.is_valid():
            new_post = serializer.save()
            if '<hr />' in new_post.body:
                new_post.truncate = len(
                    new_post.body[:new_post.body.find('<hr />')])
            else:
                new_post.truncate = 50

        if new_post.draft == False:
            new_post.published = timezone.now()
        new_post.save()

        return Response(status=201)


class PostDeleteView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()  
        return Response(status=201)


class CommentCreateView(APIView):
    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)

        if serializer.is_valid():
            new_comment = serializer.save()
        return Response(status=201)

