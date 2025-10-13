from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField()
    precio = models.IntegerField()
    stock = models.IntegerField(min=0)

class Proveedor(models.Model):
   producto = models.ForeignKey(Producto) 
   
   