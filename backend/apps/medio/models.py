from django.db import models


class Medio(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Medio"
        verbose_name_plural = "Medios"
        db_table = "medios"

    def __str__(self):
        init = "Medio{"
        end = "}"
        return f"{init} codigo:{self.codigo}, nombre:{self.nombre}, " \
               f"descripción:{self.descripcion}{end}"
