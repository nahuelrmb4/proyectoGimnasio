from django.db import models
from Actividades.models import Actividad

# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.PositiveIntegerField()
    actividades = models.ManyToManyField(
        Actividad,
        through="Clase",
        through_fields=("entrenador", "actividad")
    )

class Clase(models.Model):
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha = models.DateField()
    