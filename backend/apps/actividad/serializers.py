from rest_framework import serializers

from apps.actividad.models import Actividad
from apps.tipo_actividad.serializers import TipoActividadSerializer
from apps.user.serializers import MediumUserSerializer


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'


class ActividadReadSerializer(serializers.ModelSerializer):
    solicitante = MediumUserSerializer()
    tipo_actividad = TipoActividadSerializer()

    class Meta:
        model = Actividad
        fields = '__all__'
