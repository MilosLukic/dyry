from django.conf.urls import url
from rest_framework import routers

from api.events.views import DailyLogViewSet

router = routers.SimpleRouter()
router.register(r'events', DailyLogViewSet, base_name='events_view')


urlpatterns = [

]

urlpatterns += router.urls