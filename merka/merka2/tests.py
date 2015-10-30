from django.test import TestCase

# Create your tests here.

from merka2.models import Producto

class ProductoMethodTests(TestCase):

	def test_nombre_proyecto(self):
		per = Producto(nombre='Portatil' ,precio='120')
		per.save()
		self.assertEqual(per.nombre,'Portatil')
		self.assertEqual(per.precio,'120')

		print("Testeo correcto.")
