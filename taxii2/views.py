
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from models import Channel, Collection
from serializers import ChannelSerializer, CollectionSerializer, DiscoverySerializer


class DiscoveryView(viewsets.ViewSet):

    def list(self, request):
        d = DiscoverySerializer(data={
            'contact': 'mdavidson@soltra.com',
            'description': 'Worlds best TAXII2 Server',
            'api_bases': '/taxii/mygroup/channels/ or /taxii/mygroup/collections/ (Yes this field is really wrong)'
            })
        d.is_valid()
        return Response(d.data)


class ChannelView(viewsets.ViewSet):

    def list(self, request):
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class CollectionView(viewsets.ViewSet):

    def list(self, request):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
