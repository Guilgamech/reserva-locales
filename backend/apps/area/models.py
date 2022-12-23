from django.db import models


class Area(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        db_table = "areas"

    def __str__(self):
        init = "Area{"
        end = "}"
        return f"{init}, nombre:{self.nombre}, " \
               f"descripción:{self.descripcion}{end}"
