from rest_framework import serializers

from json_test.models import JsonTest


class JsonTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonTest
        fields = "__all__"
