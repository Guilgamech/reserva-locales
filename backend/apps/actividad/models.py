from django.db import models
from apps.aseguramiento.models import Aseguramiento
from apps.tipo_actividad.models import TipoActividad
from apps.user.models import User


class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    motivo = models.TextField(blank=True, null=True)
    solicitante = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="actividad")
    tipo_actividad = models.ForeignKey(to=TipoActividad, on_delete=models.CASCADE, related_name="actividad")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        db_table = "actividades"

    def __str__(self):
        pass
        init = "Local{"
        end = "}"
        return f"{init} nombre:{self.nombre}, motivo:{self.motivo}, " \
               f"responsable:{str(self.solicitante)}, " \
               f"tipo_actividad:{str(self.tipo_actividad)}{end}"


