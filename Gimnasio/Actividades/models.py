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
    dias = models.ManyToManyField(Dia)
    horarios = models.ManyToManyField(Horario)
    alumnos = models.ManyToManyField(Alumno)
