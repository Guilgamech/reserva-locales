from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.aseguramiento.models import Aseguramiento
from apps.aseguramiento.serializers import AseguramientoSerializer


class AseguramientoView(viewsets.ModelViewSet):
    serializer_class = AseguramientoSerializer
    queryset = Aseguramiento.objects.all()
    permission_classes = (IsAuthenticated,)
