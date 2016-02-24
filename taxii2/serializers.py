
from rest_framework import serializers
from models import Channel, Collection


class DiscoverySerializer(serializers.Serializer):
    type = serializers.CharField(default='discovery')
    contact = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=128)
    logo = serializers.CharField(max_length=128)
    api_bases = serializers.CharField(max_length=128, default='This field is wrong')


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('name', )
