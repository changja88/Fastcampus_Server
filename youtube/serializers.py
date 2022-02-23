from rest_framework import serializers

from youtube.models import Youtube


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = "__all__"
