from rest_framework import viewsets, permissions

from api.events.serializers import DailyLogSerializer


class DailyLogViewSet(viewsets.ModelViewSet):
    serializer_class = DailyLogSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.daily_logs.all()
