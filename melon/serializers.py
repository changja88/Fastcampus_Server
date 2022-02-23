from rest_framework import serializers

from json_test.models import JsonTest
from melon.models import Melon


class MelonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Melon
        fields = "__all__"
