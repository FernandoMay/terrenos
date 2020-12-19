from django.db import models

# Create your models here.
class Terrenos(models.Model):
    frente = models.DecimalField(max_digits=20,null=False,decimal_places=2)
    fondo = models.DecimalField(max_digits=20,null=False,decimal_places=2)
    precio = models.DecimalField(max_digits=20,null=False,decimal_places=2)
    name = models.CharField(max_length=100,null=False)
    imagen = models.URLField(null=False)

    def __str__(self):
        return self.name