from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)

class Inventario(models.Model):
    auto = models.ForeignKey(Auto, on_delete= models.CASCADE)
    stock = models.IntegerField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)

class Ventas(models.Model):
    auto = models.ForeignKey(Auto, on_delete= models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete= models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=11, decimal_places=2)
    iva = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
