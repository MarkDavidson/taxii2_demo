
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from models import Channel, Collection
from serializers import ChannelSerializer, CollectionSerializer, DiscoverySerializer, ApiBaseSerializer


class DiscoveryView(viewsets.ViewSet):

    def list(self, request):
        d = DiscoverySerializer(data={
            'contact': 'mdavidson@soltra.com',
            'description': 'Worlds best TAXII2 Server',
            'api_bases': [{'url': 'http://taxii2-demo.herokuapp.com/taxii/mygroup/',
                           'description': 'This is a TAXII API'}, ],
            })
        if not d.is_valid():
            return Response(d.errors)
        return Response(d.data)


class ApiBase(viewsets.ViewSet):

    def list(self, request):
        d = ApiBaseSerializer(data={
            'name': 'mygroup',
            'description': 'Worlds best API Base',
            'contact': 'mdavidson@soltra.com',
            'logo': 'https://soltra.com/favicon.ico',
            'channels': True,
            'collections': True
        })

        if not d.is_valid():
            return Response(d.errors)
        return Response(d.data)

class ChannelView(viewsets.ViewSet):

    def list(self, request):
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class CollectionView(viewsets.ViewSet):

    def list(self, request):
        collections = Collection.objects.all()
        print len(collections)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
