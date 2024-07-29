from rest_framework import serializers


class AdsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=20)
    views = serializers.IntegerField()
    pos = serializers.IntegerField()
