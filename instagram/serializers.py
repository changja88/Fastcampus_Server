from rest_framework import serializers

from instagram.models import Post
from user.models import Profile
from user.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    owner_profile = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'created', 'content', 'image', 'like_count', 'owner_profile']

    def get_owner_profile(self, obj):
        try:
            owner_profile = Profile.objects.get(user_id=obj.owner.id)
            return ProfileSerializer(owner_profile).data
        except:
            return None
