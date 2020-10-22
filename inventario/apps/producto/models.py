from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200,blank = False, null = False)
    existencia = models.IntegerField(blank = False, null = False)
    dimension = models.CharField(max_length=200, blank = False, null = False)
    descripcion = models.TextField(max_length=200, blank = False, null = False)
    lote = models.IntegerField(blank = False, null = False)
    Tipo = models.CharField(max_length=200, blank = False, null = False)
    Fecha = models.DateField(blank = False, null = True)