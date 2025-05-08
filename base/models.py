from django.db import models


class Oficina(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
