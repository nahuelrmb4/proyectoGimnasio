# Generated by Django 4.2.4 on 2023-12-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0002_alter_clase_asistencia'),
        ('Alumnos', '0002_alter_alumno_actividades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='actividades',
            field=models.ManyToManyField(blank=True, null=True, related_name='actividades', to='Actividades.actividad'),
        ),
    ]