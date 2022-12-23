from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.area.models import Area
from apps.area.serializers import AreaSerializer


class AreaView(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    permission_classes = (IsAuthenticated,)
