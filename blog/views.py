from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostListSerializer, PostDetailSerializer
from .models import Post


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
