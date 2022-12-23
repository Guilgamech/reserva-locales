from datetime import date

from rest_framework import serializers

from apps.area.models import Area
from apps.area.serializers import AreaSerializer
from apps.aseguramiento.serializers import AseguramientoSerializer
from apps.actividad.serializers import ActividadReadSerializer
from apps.local.models import Local, LocalMedio
from apps.medio.models import Medio
from apps.medio.serializers import MedioSerializer
from apps.reservacion.models import Reservacion, ReservacionAseguramiento


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'


class LocalMedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalMedio
        fields = '__all__'


class LocalMedioReadSerializer(serializers.ModelSerializer):
    medio = MedioSerializer()

    class Meta:
        model = LocalMedio
        fields = ('medio', 'cantidad')


class EditarMedioSerializer(serializers.Serializer):
    medio_id = serializers.PrimaryKeyRelatedField(queryset=Medio.objects.all())
    cantidad = serializers.IntegerField(required=False)


class ReservacionLocalAseguramientoReadSerializer(serializers.ModelSerializer):
    aseguramiento = AseguramientoSerializer()

    class Meta:
        model = ReservacionAseguramiento
        fields = ('aseguramiento', 'cantidad')


class ReservacionLocalReadSerializer(serializers.ModelSerializer):
    actividad = ActividadReadSerializer()
    aseguramientos = ReservacionLocalAseguramientoReadSerializer(
        source='reservacionaseguramientos', many=True)

    class Meta:
        model = Reservacion
        fields = '__all__'


class LocalReadSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    medios = LocalMedioReadSerializer(source='medioslocales', many=True)
    reservaciones = ReservacionLocalReadSerializer(
        source='reservacion', many=True)

    class Meta:
        model = Local
        fields = '__all__'


class LocalFullReadSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    medios = LocalMedioReadSerializer(source='medioslocales', many=True)
    reservaciones = ReservacionLocalReadSerializer(
        source='reservacion', many=True)

    class Meta:
        model = Local
        fields = '__all__'
