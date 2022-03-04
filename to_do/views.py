from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from to_do.models import ToDo
from to_do.serializers import ToDoSerializer


class ToDoSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        keyword = request.GET.get('keyword', "")
        result = ToDo.objects.filter(user=request.user, content__contains=keyword)
        return Response(ToDoSerializer(result, many=True).data)


class ToDoCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, requeset, id):
        todo = ToDo.objects.get(user=requeset.user, id=id)
        if todo.is_complete:
            todo.is_complete = False
        else:
            todo.is_complete = True
        todo.save()
        return HttpResponse(status=200)


class ToDoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        abc = ToDo.objects.filter(user=user).all()
        for a in abc:
            print(a.content)
        return Response(ToDoSerializer(ToDo.objects.filter(user=user).all(), many=True).data)

    def post(self, request):
        user = request.user
        ToDo.objects.create(
            user=user,
            content=request.POST.get('content'),
            is_complete=request.POST.get('is_complete')
        )
        return HttpResponse(status=201)
