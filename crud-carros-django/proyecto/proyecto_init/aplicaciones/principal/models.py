from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    id = models.AutoField(primary_key= True)
    tipo = models.CharField(max_length= 50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    kilometraje = models.IntegerField()
