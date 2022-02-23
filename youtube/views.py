from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from youtube.models import Youtube
from youtube.serializers import YoutubeSerializer


class YoutubeView(APIView):

    def get(self, request):
        youtube_list = Youtube.objects.all()
        serializer = YoutubeSerializer(youtube_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YoutubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
