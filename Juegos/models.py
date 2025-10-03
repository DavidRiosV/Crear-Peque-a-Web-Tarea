from django.conf import settings
from django.db import models
from django.utils import timezone

class Juegos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField()

    def __str__(self): 
        return self.nombre

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField()
    
    def __str__(self):
        return self.nombre