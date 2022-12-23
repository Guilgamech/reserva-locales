from django.db import models

from apps.actividad.models import Actividad
from apps.aseguramiento.models import Aseguramiento
from apps.local.models import Local
from apps.user.models import User


class Reservacion(models.Model):
    EstadoChoices = (
        ("Pendiente", "Pendiente"),
        ("Aprobada", "Aprobada"),
        ("Cancelada", "Cancelada"),
    )
    actividad = models.ForeignKey(
        to=Actividad, on_delete=models.CASCADE, related_name="reservacion")
    local = models.ForeignKey(
        to=Local, on_delete=models.CASCADE, related_name="reservacion")
    aseguramientos = models.ManyToManyField(
        to=Aseguramiento, through='ReservacionAseguramiento')
    estado = models.CharField(
        max_length=50, choices=EstadoChoices, default="Pendiente")
    solicitante = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="reservacion")
    cantidad_participantes = models.PositiveIntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    motivo = models.TextField(default="", blank=True)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"
        db_table = "reservacion"

    def __str__(self):
        init = "Reservacion{"
        end = "}"
        return f"{init} actividad:{str(self.actividad)}, local:{str(self.local)}, " \
               f"estado:{self.estado}, solicitante: {self.solicitante}, "\
               f"participantes: {self.cantidad_participantes}, "\
               f" fecha_inico: {str(self.fecha_inicio)}, " \
               f"fecha_fin: {str(self.fecha_fin)}{end}"


class ReservacionAseguramiento(models.Model):
    reservacion = models.ForeignKey(to=Reservacion, on_delete=models.CASCADE,
                                    related_name="reservacionaseguramientos")
    aseguramiento = models.ForeignKey(to=Aseguramiento, on_delete=models.CASCADE,
                                      related_name="reservacionaseguramientos")
    cantidad = models.PositiveIntegerField()

    class Meta:
        unique_together = [['reservacion', 'aseguramiento']]
        verbose_name = "ReservacionAseguramiento"
        verbose_name_plural = "ReservacionAseguramientos"
        db_table = "reservacion_aseguramiento"

    def __str__(self):
        init = "ReservacionAseguramiento{"
        end = "}"
        return f"{init} actividad:{str(self.reservacion)}, aseguramiento:{str(self.aseguramiento)}, " \
               f"cantidad:{self.cantidad}{end}"
