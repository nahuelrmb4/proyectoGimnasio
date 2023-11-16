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

    def __str__(self):
        return self.apellido

    class Meta:
        ordering = ['apellido']

class Clase(models.Model):
    fecha = models.DateField(auto_now_add=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    asistencia = models.CharField(max_length=20, null=True, blank=True, default='sin registro')
    
    
    
    
    