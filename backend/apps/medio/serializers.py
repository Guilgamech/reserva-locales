from rest_framework import serializers

from apps.medio.models import Medio


class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = '__all__'