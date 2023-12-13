# Generated by Django 4.2.4 on 2023-12-13 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0002_alter_clase_asistencia'),
        ('Alumnos', '0003_alter_alumno_actividades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='actividades',
            field=models.ManyToManyField(blank=True, null=True, to='Actividades.actividad'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Alumnos.plan'),
        ),
    ]