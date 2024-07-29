import json

from django.http import HttpResponseBadRequest
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Ads
from .serializers import AdsSerializer


class GetAdsInfoView(APIView):
    def get(self, request):
        try:
            id = dict(request.GET)['id']
            print(id)
            queryset = Ads.objects.filter(ad_id__in=id)
            # Сериализуем извлечённый набор записей
            serializer_for_queryset = AdsSerializer(
                    instance=queryset,  # Передаём набор записей
                    many=True  # Указываем, что на вход подаётся именно набор записей
                )

            return Response(serializer_for_queryset.data)
        except:
            return HttpResponseBadRequest()

