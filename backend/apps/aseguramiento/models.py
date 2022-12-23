from django.db import models


class Aseguramiento(models.Model):
    nombre = models.CharField(max_length=10)
    descripcion = models.TextField(blank=True, null=True)
    responsable_email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = "Aseguramiento"
        verbose_name_plural = "Aseguramientos"
        db_table = "aseguramientos"

    def __str__(self):
        init = "Aseguramiento{"
        end = "}"
        return f"{init} nombre:{self.nombre}, descripcion:{self.descripcion}, " \
               f"responsable_email:{self.responsable_email}{end}"
