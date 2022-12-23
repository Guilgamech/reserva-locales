from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.medio.models import Medio
from apps.medio.serializers import MedioSerializer


class MedioView(viewsets.ModelViewSet):
    serializer_class = MedioSerializer
    queryset = Medio.objects.all()
    permission_classes = (IsAuthenticated,)
