from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.actividad.serializers import ActividadReadSerializer
from apps.aseguramiento.models import Aseguramiento
from apps.aseguramiento.serializers import AseguramientoSerializer
from apps.local.models import Local
from apps.local.serializers import LocalReadSerializer, LocalSerializer
from apps.reservacion.models import Reservacion, ReservacionAseguramiento
from apps.user.serializers import MediumUserSerializer


# Reservacion serializers y serializerRead
class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'

    def update(self, instance: Reservacion, validated_data: dict):
        if instance.fecha_inicio != validated_data.get("fecha_inicio") or \
                instance.fecha_fin != validated_data.get("fecha_fin"):
            validated_data["estado"] = "Pendiente"
        return super().update(instance, validated_data)


class ReservacionAseguramientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservacionAseguramiento
        fields = '__all__'


class ReservacionAseguramientoReadSerializer(serializers.ModelSerializer):
    aseguramiento = AseguramientoSerializer()

    class Meta:
        model = ReservacionAseguramiento
        fields = ('id', 'aseguramiento', 'cantidad')


class ReservacionReadSerializer(serializers.ModelSerializer):
    solicitante = MediumUserSerializer()
    local = LocalSerializer()
    aseguramientos = ReservacionAseguramientoReadSerializer(source='reservacionaseguramientos', many=True)
    actividad = ActividadReadSerializer()

    class Meta:
        model = Reservacion
        fields = '__all__'


class EditarAseguramientoSerializer(serializers.Serializer):
    aseguramiento_id = serializers.PrimaryKeyRelatedField(
        queryset=Aseguramiento.objects.all())
    cantidad = serializers.IntegerField(required=False)


class EliminarAseguramientoSerializer(serializers.Serializer):
    aseguramiento_id = serializers.PrimaryKeyRelatedField(
        queryset=Aseguramiento.objects.all())