#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_Merka.settings')

import django
django.setup()

from merka.models import Seccion, Producto


def populate():
    teles = add_Seccion('TELEVISORES')

    add_Producto(seccion=teles, nombre="P1", precio="100", imagen="Folder.jpg")
    add_Producto(seccion=teles, nombre="tele1", precio="300", imagen="img1.jpg")
    add_Producto(seccion=teles, nombre="tele2", precio="200", imagen="img2.jpg")
    add_Producto(seccion=teles, nombre="tele3", precio="100", imagen="img3.jpg")

    portatiles =add_Seccion('PORTÁTILES')

    add_Producto(seccion=portatiles, nombre="portatil1", precio="500", imagen="img4.jpg")

    Sobremesas = add_Seccion('SOBREMESAS')

    moviles = add_Seccion('MÓVILES')

    perifericos = add_Seccion('PERIFÉRICOS')

    tabletas = add_Seccion('TABLETAS')

    # Print out what we have added to the user.
    for s in Seccion.objects.all():
        for p in Producto.objects.filter(seccion=s):
            print "- {0} - {1}".format(str(s), str(p))

def add_Producto(seccion, nombre, precio, imagen):
    p = Producto.objects.get_or_create(seccion=seccion, nombre=nombre)[0]
    p.precio=precio
    p.imagen=imagen
    p.save()
    return p

def add_Seccion(nombre):
    s = Seccion.objects.get_or_create(nombre=nombre)[0]
    s.save()
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting Merka population script..."
    populate()
