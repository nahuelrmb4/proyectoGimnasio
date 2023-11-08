from django.db import models
from Alumnos.models import Alumno

# Create your models here.

class Dia(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    horario = models.CharField(max_length=50)

    def __str__(self):
        return self.horario 

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno)
