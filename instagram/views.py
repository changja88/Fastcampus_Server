from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.serializers import PostSerializer
from instagram.models import Post


class InstagramPostUpload(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InstagramPostList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(owner=user)


class InstagramPostAll(APIView):

    def get(self, reqeust):
        post_list_all = Post.objects.all()
        serializer = PostSerializer(post_list_all, many=True)
        return Response(serializer.data)


class InstagramPostLike(APIView):

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.like_count += 1
        post.save()
        return HttpResponse(
            status=201
        )
