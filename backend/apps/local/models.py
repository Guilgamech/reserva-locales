from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError

from apps.area.models import Area
from apps.helper.helper import NestedViewSetMixin
from apps.medio.models import Medio



class Local(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    telefono = PhoneNumberField(unique=True, null=False, blank=False)
    responsable_email = models.EmailField(blank=True, null=True)
    area = models.ForeignKey(to=Area, on_delete=models.CASCADE, related_name="localarea")
    medios = models.ManyToManyField(to=Medio, through='LocalMedio')

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"
        db_table = "locales"

    def __str__(self):
        pass
        init = "Local{"
        end = "}"
        return f"{init} nombre:{self.nombre}, capacidad:{self.capacidad}, " \
               f"telefono:{self.telefono}, responsable_email:{self.responsable_email}, " \
               f"area:{str(self.area)}{end}"


class LocalMedio(models.Model):
    local = models.ForeignKey(to=Local, on_delete=models.CASCADE, related_name="medioslocales")
    medio = models.ForeignKey(to=Medio, on_delete=models.CASCADE, related_name="medioslocales")
    cantidad = models.PositiveIntegerField()

    class Meta:
        unique_together = [['local', 'medio']]
        verbose_name = "LocalMedio"
        verbose_name_plural = "LocalMedios"
        db_table = "local_medio"


    def __str__(self):
        init = "LocalMedio{"
        end = "}"
        return f"{init} local:{str(self.local)}, medio:{str(self.medio)}, " \
               f"cantidad:{self.cantidad}{end}"


