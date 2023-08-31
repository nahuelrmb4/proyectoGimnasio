from django.db import models

# Create your models here.

class Producto(models.Model):
    #Campos/Atributos definidos a través de recursos de la clase base para después poder ser validados con los métodos propios de la clase.
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre