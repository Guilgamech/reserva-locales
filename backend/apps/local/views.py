from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.helper.helper import NestedViewSetMixin
from apps.local.models import Local, LocalMedio
from apps.local.serializers import LocalSerializer, LocalMedioSerializer, LocalReadSerializer, LocalFullReadSerializer, \
    EditarMedioSerializer
from apps.reservacion.serializers import ReservacionSerializer


class LocalReservacionView(NestedViewSetMixin):
    serializer_class = LocalSerializer
    queryset = Local.objects.all().prefetch_related('reservacion')
    read_serializer_class = LocalReadSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        params = self.request.query_params
        responsable_email = params.get("responsable_email")
        local_id = params.get("local_id")
        if responsable_email is not None:
            return Local.objects.filter(responsable_email=responsable_email)
        if local_id is not None:
            return Local.objects.filter(pk=local_id)
        return super().get_queryset()




class LocalMedioView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = LocalMedioSerializer
    queryset = LocalMedio.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        if request.data["local"] is not None:
            local_id = request.data["local"]
            local = Local.objects.filter(pk=local_id).first()
            if local is not None and self.request.user.email != local.responsable_email:
                raise PermissionDenied()
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.data["local"] is not None:
            local_id = request.data["local"]
            local = Local.objects.filter(pk=local_id).first()
            if local is not None and self.request.user.email != local.responsable_email:
                raise PermissionDenied()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.data["local"] is not None:
            local_id = request.data["local"]
            local = Local.objects.filter(pk=local_id).first()
            if local is not None and self.request.user.email != local.responsable_email:
                raise PermissionDenied()
        return super().destroy(request, *args, **kwargs)


class LocalView(NestedViewSetMixin):
    serializer_class = LocalSerializer
    queryset = Local.objects.all()
    read_serializer_class = LocalFullReadSerializer
    permission_classes = (IsAuthenticated, )


    @action(detail=False, methods=["get"])
    def responsables(self, request):
        user = self.request.user
        locales = Local.objects.filter(responsable_email=user.email)
        data = LocalFullReadSerializer(instance=locales, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=True, url_path='modificar-medio', methods=["put"], serializer_class=EditarMedioSerializer)
    def actulizar_medio(self, request, pk=None, *args, **kwargs):
        sr = EditarMedioSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        medio = sr.validated_data.get("medio_id")
        cantidad = sr.validated_data.get("cantidad")
        local = self.get_object()
        local.medios.remove(medio)
        local.medios.add(medio, through_defaults={'cantidad': cantidad})
        data = LocalFullReadSerializer(instance=local).data
        return Response(data, status=status.HTTP_200_OK)


    @action(detail=True, url_path='eliminar-medio', methods=["post"], serializer_class=EditarMedioSerializer)
    def eliminar_medio(self, request, pk=None, *args, **kwargs):
        sr = EditarMedioSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        medio = sr.validated_data.get("medio_id")
        local = self.get_object()
        local.medios.remove(medio)
        return Response(None, status=status.HTTP_205_RESET_CONTENT)
