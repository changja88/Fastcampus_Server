from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from json_test.models import JsonTest
from json_test.serializers import JsonTestSerializer




class JsonTestView(APIView):

    def get(self, request):
        JsonTests = JsonTest.objects.all()
        serializer = JsonTestSerializer(JsonTests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JsonTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
