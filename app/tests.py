#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase
from merka.models import Seccion, Producto
from django.core.urlresolvers import reverse

# Create your tests here.

def add_sec(nombre):
	s = Seccion.objects.get_or_create(nombre=nombre)[0]
	s.save()
	return s

class SeccionMethodTests(TestCase):

	def test_crear_seccion(self):
		consolas = add_sec('CONSOLAS')
		self.assertEqual(consolas.nombre,'CONSOLAS' )
		print("Test: Creación de una nueva seccion correcta")

class ProductoMethodTests(TestCase):
	def test_crear_producto(self):
		consolas = Seccion(nombre="CONSOLAS")
		p = Producto(seccion=consolas, nombre="xbox")
		p.precio="350"
		p.imagen="imagen.jpg"
		p.save()
		self.assertEqual(consolas, p.seccion)
		print("Test: Creacion de un nuevo producto Correcto")



class IndexViewTests(TestCase):

	def test_index_view_with_no_secciones(self):
		"""
		If no questions exist, an appropriate message should be displayed.
		"""
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No hay Secciones presentes")
		self.assertQuerysetEqual(response.context['secciones'], [])
		print("Test:Petición a la portada sin secciones Correcta")



	def test_index_view_with_secciones(self):
		"""
		If no questions exist, an appropriate message should be displayed.
		"""
		add_sec('test')
		add_sec('temp')
		add_sec('tmp')
		add_sec('tmp test temp')
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "tmp test temp")
		num_secs =len(response.context['secciones'])
		self.assertEqual(num_secs , 4)
		print("Test:Petición a la portada con secciones Correcta")
