from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Profile
from user.serializers import UserSerializer, ProfileSerializer


@csrf_exempt
def SingupAPI(request):
    if request.method == "POST":
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "error": "존재하는 유저 입니다",
            })

        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(
                username=username,
                password=password
            )
            token = Token.objects.create(user=user)
            auth.login(request, user)

            Profile.objects.get_or_create(user_id=user.id)

            return JsonResponse({
                "id" : user.id,
                "username": username,
                "token": token.key
            })
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def LoginAPI(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            token = Token.objects.get(user=user)
            return JsonResponse({
                "id" : user.id,
                "token": token.key
            })

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserInfoAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user_id'

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user_id=user.id)
