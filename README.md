## **Proyecto de infraestructura virtual junto con desarrollo de aplicaciones para Internet** ##

## **Hito 1: Merka** ##

### **Participantes:** ###

### Ángel Valera Motos  ###
### Bogdan Alin Muresan ###

**Descripción:**

Nuestra aplicación se trata de un sistema de gestión de paquetes, de modo que la aplicación web será una tienda online, desarrollada en python, en un framework de alto nivel como Django. Dicha tienda consistirá en que tu puedes comprar algún tipo de producto, realizar un seguimiento de dicho producto.

El proyecto se va a desarrollar en dos módulos, dentro de un repositorio principal de  tipo [organización](https://github.com/ProyectoIV-DAI/ProyectoIV-Modulo-Principal.git):

**El módulo 1:**  [(Ángel Valera Motos )](https://github.com/AngelValera/proyectoIV-Modulo-1.git)Este módulo se encarga de toda la gestión de las bases de datos necesarias. Al tratarse de una tienda online necesitaremos base de datos (MySQL) replicadas, una base de datos para usuarios, para productos, etc. 

**El módulo 2:** [(Bogdan Alin Muresan )](https://github.com/bogdananas/proyectoIV-modulo2.git) Este módulo se encarga del alojamiento web de la aplicación, en el servidor así como la conexión de la aplicación con las bases de datos y el despliegue de la misma.

Hemos elegido llevar a cabo este proyecto, porque se centra en la virtualización de recursos como puede ser el uso de máquinas virtuales para el despliegue de una aplicación para Internet, usando también para ello un framework de alto nivel.

Estamos inscritos en el certamen de proyectos de la UGR organizado por la OSL.

## **Hito 2: Merka** ##

He usado el framework Django, ya que decidimos hacer la aplicación en Python.

El código muestra una sencilla página de inicio a la cual le pasamos un test de comprobación, de manera que se irá mejorando a lo largo del desarrollo del proyecto.

La automatización  se puede ver en este makefile:

```
#Makefile Angel Valera Motos
#clean install test run doc

clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;

install:
	python setup.py install

test:
	python manage.py test

run:
	python manage.py runserver
doc:
	epydoc --html merka2/views.py merka2/models.py
```
Para la interacción continua he usado travis ya que es el que usé para el desarrollo de los ejercicios del tema 2.
El archivo travis.yml contiene lo siguiente:

```
language: python
python:
 - "2.7"
before_install:
 - cd merka
# command to install dependencies
install:
 - make install

# command to run tests para django python
script:
 - make tests
```

![resultado del test](https://travis-ci.org/AngelValera/proyectoIV-Modulo-1.svg?branch=master)