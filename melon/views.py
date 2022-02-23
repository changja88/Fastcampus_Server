from rest_framework.response import Response
from rest_framework.views import APIView

from melon.models import Melon
from melon.serializers import MelonSerializer


class MelonView(APIView):

    def get(self, request):
        melon_list = Melon.objects.all()
        serializer = MelonSerializer(melon_list, many=True)
        return Response(serializer.data)
