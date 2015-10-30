from django.db import models

class Producto(models.Model):

	nombre = models.CharField(max_length=50)
	precio = models.CharField(max_length=9)


	def __unicode__(self):
		return self.nombre
