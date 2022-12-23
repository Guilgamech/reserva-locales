# Generated by Django 3.2.13 on 2022-12-13 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='reservacionaseguramiento',
            unique_together={('reservacion', 'aseguramiento')},
        ),
    ]