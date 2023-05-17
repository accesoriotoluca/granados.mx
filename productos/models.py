from django.db import models

class Productos(models.Model):
    
    Producto = models.CharField(max_length=120)

    Precio = models.FloatField()
    Costo = models.FloatField()

    Foto_1 = models.CharField(max_length=120)
    Foto_2 = models.CharField(max_length=120)
    Foto_3 = models.CharField(max_length=120)
    Foto_4 = models.CharField(max_length=120)

    Género = models.CharField(max_length=120)
    Talla = models.CharField(max_length=120)
    Marca = models.CharField(max_length=120)
    Color = models.CharField(max_length=120)
    Detalle = models.CharField(max_length=120)
    características = models.CharField(max_length=120)
    

    Fecha_Creación = models.DateTimeField(auto_now_add=True)
    Fecha_Actualización = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"
