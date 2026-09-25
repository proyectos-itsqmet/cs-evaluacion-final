from django.db import models

class Telefono(models.Model):
    nombre = models.CharField(max_length = 255)
    marca = models.CharField(max_length = 255)
    descripcion = models.TextField()
    imagen = models.URLField()
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    almacenamiento = models.CharField(max_length = 255)
    ram = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255, default = "", blank = True)
    stock = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"{self.marca} {self.nombre}"
