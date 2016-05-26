from django.contrib import admin

from apps.events.models import TextEvent, ImageEvent, ValueEvent, EventGroup, DailyLog, EventsPost


class TextEventAdmin(admin.ModelAdmin):
    list_display = ['events_post', 'created', 'text']


class ImageEventAdmin(admin.ModelAdmin):
    list_display = ['events_post', 'created', 'url', 'comment']


class ValueEventAdmin(admin.ModelAdmin):
    list_display = ['events_post', 'created', 'value', 'metric']


class EventGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class DailyLogAdmin(admin.ModelAdmin):
    list_display = ['date', 'user']


class EventsPostAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'daily_log', 'created', 'group']

admin.site.register(TextEvent, TextEventAdmin)
admin.site.register(ImageEvent, ImageEventAdmin)
admin.site.register(ValueEvent, ValueEventAdmin)
admin.site.register(EventGroup, EventGroupAdmin)
admin.site.register(DailyLog, DailyLogAdmin)
admin.site.register(EventsPost, EventsPostAdmin)