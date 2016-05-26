from rest_framework import serializers
from apps.events.models import DailyLog, ValueEvent, TextEvent, ImageEvent
from apps.misc.models import Metric


class DailyLogSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = DailyLog
        fields = ['date', 'events']

    def get_events(self, obj):
        events = obj.events.all().prefetch_related('textevents', 'valueevents', 'imageevents').order_by('-timestamp')[:10]
        serialized_events = []
        for event in events:
            for text_event in event.textevents.all():
                serialized_events.append(TextEventSerializer(text_event).data)

            for value_event in event.valueevents.all():
                serialized_events.append(ValueEventSerializer(value_event).data)

            for image_event in event.imageevents.all():
                serialized_events.append(ImageEventSerializer(image_event).data)

        return serialized_events


class TextEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEvent


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric


class ValueEventSerializer(serializers.ModelSerializer):
    metric = MetricSerializer()

    class Meta:
        model = ValueEvent


class ImageEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEvent
