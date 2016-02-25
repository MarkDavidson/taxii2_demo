
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    contact = models.CharField(max_length=128, default='mdavidson@soltra.com')
    subscription = models.BooleanField(default=False)
    auth = models.CharField(max_length=128, default='???')
    conn_limits = models.IntegerField(null=True, default=10)
    idle_timeout = models.IntegerField(null=True, default=3600)
    max_post_msg_size = models.IntegerField(null=True, default=10000)
    max_get_msg_size = models.IntegerField(null=True, default=10000)
    msg_age = models.IntegerField(null=True, default=10000)
    queue_size = models.IntegerField(null=True, default=50)
    subscribers = models.CharField(max_length=128, default='Field not implemented yet')
    can_read = models.BooleanField(default=True)


class Collection(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
