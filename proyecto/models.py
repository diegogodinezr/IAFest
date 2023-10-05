from django.db import models
from django.utils import timezone

# Create your models here.
class Tabla(models.Model):
    id = models.AutoField(primary_key=True)
    id_registro = models.CharField(max_length=10)
    fecha_ingreso = models.DateField(default=None) 
    fecha_sintomas = models.DateField(default=None) 
    edad = models.IntegerField()
    pais_nacimiento = models.CharField(max_length=50)