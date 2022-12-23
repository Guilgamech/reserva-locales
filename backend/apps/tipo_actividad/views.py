from django.shortcuts import render

from rest_framework import status, viewsets, mixins

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from apps.tipo_actividad.models import TipoActividad
from apps.tipo_actividad.serializers import TipoActividadSerializer


class TipoActividadView(viewsets.ModelViewSet):
    serializer_class = TipoActividadSerializer
    queryset = TipoActividad.objects.all()
    permission_classes = (IsAuthenticated,)


