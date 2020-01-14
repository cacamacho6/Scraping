from django.conf import settings
from django.db import models

class Producto(models.Model):
    titulo = models.CharField()
    precio = models.CharField()
    envio = models.CharField()
    def _str_(self):
        return self.titulo 


