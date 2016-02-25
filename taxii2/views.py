
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from models import Channel, Collection
from serializers import ChannelSerializer, CollectionSerializer, \
                        DiscoverySerializer, ApiBaseSerializer, IndicatorSerializer


class DiscoveryView(viewsets.ViewSet):

    def list(self, request):
        d = DiscoverySerializer(data={
            'contact': 'mdavidson@soltra.com',
            'description': 'Worlds best TAXII2 Server',
            'api_bases': [{'url': 'http://taxii2-demo.soltra.com/taxii/mygroup/',
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


class IndicatorView(viewsets.ViewSet):

    def list(self, request):
        d = IndicatorSerializer(data={
                "type": "indicator",
                "id": "indicator--089a6ecb-cc15-43cc-9494-767639779123",
                "spec_version": "2.0",
                "created_at": "2016-02-19T09:11:01Z",
                "description": "file used by malware x",
                "indicator_types": [ "malware" ],
                "observables": [
                    {
                    "type": "file-object",
                    "hashes": [ {
                        "type": "md5",
                        "hash_value": "3773a88f65a5e780c8dff9cdc3a056f3"
                        } ],
                    "size": 25537
                    }],
                })
        if not d.is_valid():
            return Response(d.errors)
        return Response(d.data)