from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Profile


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

    def get_profile(self, obj):
        try:
            owner_profile = Profile.objects.get(user_id=obj.id)
            return ProfileSerializer(owner_profile).data
        except:
            return None
