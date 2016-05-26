from django.contrib import admin


from apps.misc.models import Metric


class MetricAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'discrete', 'units', 'code']
    search_fields = ['name', 'code']

admin.site.register(Metric, MetricAdmin)
