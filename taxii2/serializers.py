
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
    x_channels_url = serializers.CharField(default='http://taxii2-demo.soltra.com/taxii/mygroup/channels/')
    collections = serializers.BooleanField(default=True)
    x_collections_url = serializers.CharField(default='http://taxii2-demo.soltra.com/taxii/mygroup/collections/')


class HashSerializer(serializers.Serializer):
    type = serializers.CharField(default='md5')
    hash_value = serializers.CharField()


class FileObservableSerializer(serializers.Serializer):
    type = serializers.CharField(default='file-object')
    hashes = HashSerializer(many=True)
    size = serializers.IntegerField()


class IndicatorSerializer(serializers.Serializer):
    type = serializers.CharField(default='indicator')
    id = serializers.CharField()
    spec_version = serializers.CharField()
    created_at = serializers.CharField()
    description = serializers.CharField()
    indicator_types = serializers.ListField()
    observables = FileObservableSerializer(many=True)


class ChannelSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, slug):
        return 'channel-info'

    class Meta:
        model = Channel
        fields = ('type', 'name', 'description', 'contact', 'subscription', 'auth', 'conn_limits',
                  'idle_timeout', 'max_post_msg_size', 'max_get_msg_size', 'msg_age',
                  'queue_size', 'subscribers', 'can_read')


class CollectionSerializer(serializers.ModelSerializer):

    type = serializers.SerializerMethodField()
    x_info = serializers.SerializerMethodField()

    def get_type(self, slug):
        return 'collection-info'

    def get_x_info(self, slug):
        return 'Collections do not currently have much information in the spec, so they are sparse here'

    class Meta:
        model = Collection
        fields = ('type', 'name', 'description', 'x_info')

