
from rest_framework import serializers
from models import Channel, Collection


class DiscoveryApiBaseSerializer(serializers.Serializer):
    url = serializers.CharField()
    description = serializers.CharField()


class DiscoverySerializer(serializers.Serializer):
    type = serializers.CharField(default='discovery')
    contact = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=128)
    logo = serializers.CharField(max_length=128, required=False)
    api_bases = DiscoveryApiBaseSerializer(many=True)


class ApiBaseSerializer(serializers.Serializer):
    type = serializers.CharField(default='api-info')
    name = serializers.CharField()
    description = serializers.CharField()
    contact = serializers.CharField()
    logo = serializers.CharField(default='https://soltra.com/favicon.ico')
    channels = serializers.BooleanField(default=True)
    collections = serializers.BooleanField(default=True)


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('name', )
