from django.db import models
from django.template.defaultfilters import slugify




# Create your models here.
class Seccion(models.Model):
    nombre = models.CharField(max_length=128, primary_key=True, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Seccion, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    seccion = models.ForeignKey(Seccion)
    nombre = models.CharField(max_length=128,  primary_key=True, unique=True)
    precio = models.IntegerField(default=0)
    imagen = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre
