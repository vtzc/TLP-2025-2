from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField(min=0)
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
   producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
   
   
   