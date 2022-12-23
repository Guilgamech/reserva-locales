from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.actividad.models import Actividad
from apps.actividad.serializers import ActividadSerializer, ActividadReadSerializer
from apps.helper.helper import NestedViewSetMixin


class ActividadView(NestedViewSetMixin):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()
    read_serializer_class = ActividadReadSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        actividades = Actividad.objects.filter(solicitante=self.request.user)
        data = ActividadReadSerializer(instance=actividades, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
