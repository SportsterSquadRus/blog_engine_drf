from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from .models import Post
from django.utils import timezone


class PostsListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(draft=False)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetialView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk, draft=False)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostCreateView(APIView):
    def post(self, request):
        post = PostCreateSerializer(data=request.data)

        if post.is_valid():
            new_post = post.save()
            if '<hr />' in new_post.body:
                new_post.truncate = len(
                    new_post.body[:new_post.body.find('<hr />')])
            else:
                new_post.truncate = 50

        if new_post.draft == False:
            new_post.published = timezone.now()
        new_post.save()

        return Response(status=201)

