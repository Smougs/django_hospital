from django.db import models

# Create your models here.

class medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    stock = models.IntegerField()
    def __str__(self):
        return self.nombre


class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class venta(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    def __str__(self):
        return self.cliente.nombre

class proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
