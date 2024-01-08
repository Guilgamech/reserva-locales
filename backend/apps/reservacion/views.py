from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from apps.helper.helper import NestedViewSetMixin
from apps.helper.messages import email_reserva, email_reserva_state
from apps.reservacion.models import Reservacion, ReservacionAseguramiento
from apps.reservacion.serializers import ReservacionSerializer, \
    ReservacionAseguramientoSerializer, ReservacionReadSerializer, Local, EditarAseguramientoSerializer, \
    EliminarAseguramientoSerializer
from apps.helper.functions import checkDateInRange
from datetime import timedelta, datetime
from apps.user.models import User
from apps.local.models import Local


class ReservacionView(NestedViewSetMixin):
    serializer_class = ReservacionSerializer
    queryset = Reservacion.objects.all()
    read_serializer_class = ReservacionReadSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        print(request.data)
        solicitante = request.data.get('solicitante')
        local = request.data.get('local')
        if solicitante and local:
            reservaciones = list(Reservacion.objects.filter(
                solicitante_id=request.data.get('solicitante'),
                local_id=request.data.get('local')))
            reservaciones_aprobadas = list(
                Reservacion.objects.filter(estado="Aprobada"))
            reservaciones.extend(reservaciones_aprobadas)
            if len(reservaciones) > 0 and request.data.get('fecha_inicio') and request.data.get('fecha_fin'):
                fecha_inicio = request.data.get('fecha_inicio')
                fecha_fin = request.data.get('fecha_fin')
                newStart = datetime.fromisoformat(
                    fecha_inicio) + timedelta(seconds=1)
                newEnd = datetime.fromisoformat(
                    fecha_fin) - timedelta(seconds=1)
                """
                (newStart < elStart && elStart < newEnd) ||
                (newStart < elEnd && elEnd < newEnd) ||
                (elStart < newStart && newStart < elEnd) ||
                (elStart < newEnd && newEnd < elEnd)
                """
                def foundDateInRange(element: Reservacion):
                    if checkDateInRange(element.fecha_inicio, newStart, newEnd):
                        return True
                    if checkDateInRange(element.fecha_fin, newStart, newEnd):
                        return True
                    if checkDateInRange(newStart, element.fecha_inicio, element.fecha_fin):
                        return True
                    if checkDateInRange(newEnd, element.fecha_inicio, element.fecha_fin):
                        return True
                    return False

                found = list(filter(foundDateInRange, reservaciones))
                if len(found) > 0:
                    raise ValidationError(
                        {"fecha_inico": ["ya tiene una reservación en esa fecha"]})
            solicitante_obj = User.objects.filter(pk=solicitante).first()
            local_obj = Local.objects.filter(pk=local).first()
            if solicitante_obj and local_obj:
                email_reserva(solicitante_obj, local_obj)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        estado = request.data.get("estado")
        motivo = request.data.get("motivo")
        local_id = request.data.get("local")
        if local_id is not None and estado is not None and estado == "Aprobada":
            local = Local.objects.filter(pk=local_id).first()
            if local is None:
                raise ValidationError(
                    {"local": [f"Local con id:{local_id} no esta en la base de datos"]})
            if local.responsable_email != user.email:
                raise PermissionDenied()
            reservacion = self.get_object()
            reservaciones_aprobadas = list(
                Reservacion.objects.filter(estado="Aprobada"))
            if len(reservaciones_aprobadas) > 0:
                newStart = reservacion.fecha_inicio + timedelta(seconds=1)
                print(newStart)
                newEnd = reservacion.fecha_fin - timedelta(seconds=1)
                print(newEnd)

                def foundDateInRange(element: Reservacion):
                    if checkDateInRange(element.fecha_inicio, newStart, newEnd):
                        return True
                    if checkDateInRange(element.fecha_fin, newStart, newEnd):
                        return True
                    if checkDateInRange(newStart, element.fecha_inicio, element.fecha_fin):
                        return True
                    if checkDateInRange(newEnd, element.fecha_inicio, element.fecha_fin):
                        return True
                    return False

                found = list(filter(foundDateInRange, reservaciones_aprobadas))
                print(found)
                if len(found) > 0:
                    raise ValidationError(
                        {"fecha_inico": ["ya tiene una reservación en esa fecha"]})
            email_reserva_state(reservacion, user)
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def responsables(self, request):
        user = self.request.user
        reservaciones = Reservacion.objects.filter(
            local__responsable_email=user.email)
        data = ReservacionReadSerializer(
            instance=reservaciones, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def solitante(self, request):
        user = self.request.user
        reservaciones = Reservacion.objects.filter(solicitante=user)
        data = ReservacionReadSerializer(
            instance=reservaciones, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def aprobadas(self, request):
        user = self.request.user
        reservaciones_aprobadas = (Reservacion.objects.filter(
            estado="Aprobada",
            solicitante=user
        ))
        data = ReservacionReadSerializer(instance=reservaciones_aprobadas, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=True, url_path='modificar-aseguramiento', methods=["put"],
            serializer_class=EditarAseguramientoSerializer)

    def actulizar_aseguramiento(self, request, pk=None, *args, **kwargs):
        sr = EditarAseguramientoSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        aseguramiento = sr.validated_data.get("aseguramiento_id")
        cantidad = sr.validated_data.get("cantidad")
        reservacion = self.get_object()
        reservacion.aseguramientos.remove(aseguramiento)
        reservacion.aseguramientos.add(
            aseguramiento, through_defaults={'cantidad': cantidad})
        data = ReservacionReadSerializer(instance=reservacion).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, url_path='eliminar-aseguramiento', methods=["post"],
            serializer_class=EliminarAseguramientoSerializer)
    def eliminar_aseguramiento(self, request, pk=None, *args, **kwargs):
        sr = EliminarAseguramientoSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        aseguramiento = sr.validated_data.get("aseguramiento_id")
        reservacion = self.get_object()
        reservacion.aseguramientos.remove(aseguramiento)
        return Response(None, status=status.HTTP_205_RESET_CONTENT)
    
    @action(detail=True, url_path='aprobar')
    def aprobar(self, request, pk=None, *args, **kwargs):
        reservacion = self.get_object()
        reservacion.estado = 'Aprobada'
        reservacion.save()
        return Response(None, status=status.HTTP_205_RESET_CONTENT)


class ReservacionAseguramientoView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    serializer_class = ReservacionAseguramientoSerializer
    queryset = ReservacionAseguramiento.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.data["reservacion"] is not None:
            reservacion_id = request.data["reservacion"]
            reservacion = Reservacion.objects.filter(pk=reservacion_id).first()
            if reservacion is not None and self.request.user.id != reservacion.solicitante_id:
                raise PermissionDenied()
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.data["reservacion"] is not None:
            reservacion_id = request.data["reservacion"]
            reservacion = Reservacion.objects.filter(pk=reservacion_id).first()
            if reservacion is not None and self.request.user.id != reservacion.solicitante_id:
                raise PermissionDenied()
        return super().update(request, *args, **kwargs)
