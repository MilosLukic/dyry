import datetime

from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models

from apps.misc.models import Metric


class DailyLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, related_name='daily_logs')


class EventGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class EventsPost(models.Model):
    timestamp = models.DateTimeField(default=now)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    daily_log = models.ForeignKey(DailyLog, related_name='events')
    group = models.ForeignKey(EventGroup, related_name='events', blank=True, null=True)

    def __str__(self):
        return str(self.timestamp)


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    events_post = models.ForeignKey(EventsPost, related_name='%(class)ss')

    class Meta:
        abstract = True


class TextEvent(Event):
    text = models.TextField()


class ImageEvent(Event):
    url = models.URLField()
    comment = models.TextField(null=True, blank=True)


class ValueEvent(Event):
    value = models.CharField(max_length=255)
    metric = models.ForeignKey(Metric)
    comment = models.CharField(max_length=255)
