![resultado del test](https://travis-ci.org/AngelValera/proyectoIV-Modulo-1.svg?branch=master)

![snap-ci](https://snap-ci.com/AngelValera/proyectoIV-Modulo-1/branch/master/build_image)

#**MERKA:TIENDA ONLINE**#
## **Proyecto de infraestructura virtual junto con desarrollo de aplicaciones para Internet** ##

**Descripción:**

Nuestra aplicación se trata de un sistema de gestión de paquetes, de modo que la aplicación web será una tienda online, desarrollada en python, en un framework de alto nivel como Django. Dicha tienda consistirá en que tu puedes comprar algún tipo de producto, realizar un seguimiento de dicho producto.

El proyecto se va a desarrollar en dos módulos, dentro de un repositorio principal de  tipo [organización](https://github.com/ProyectoIV-DAI/ProyectoIV-Modulo-Principal.git):

**El módulo 1:**  [(Ángel Valera Motos )](https://github.com/AngelValera/proyectoIV-Modulo-1.git)Este módulo se encarga de toda la gestión de las bases de datos necesarias. Al tratarse de una tienda online necesitaremos base de datos replicadas, una base de datos para usuarios, para productos, etc. 

Hemos elegido llevar a cabo este proyecto, porque se centra en la virtualización de recursos como puede ser el uso de máquinas virtuales para el despliegue de una aplicación para Internet, usando también para ello un framework de alto nivel.

**Estamos inscritos en el certamen de proyectos de la UGR organizado por la OSL.**

##**Herramienta de Construcción**##
He usado el framework Django, ya que decidimos hacer la aplicación en Python, por tanto usaremos las herramientas que proporciona, siendo estas manage.py y setup.py.

Además se añaden los archivos **[docker.sh](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Scripts/docker.sh)**, **[heroku.sh](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Scripts/heroku.sh)** y **[ejecutar_App.sh](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Scripts/ejecutar_App.sh)** para la construcción de un entorno seguro (contenedor Docker), su posterior despliegue automático en el PAAS de Heroku y el arranque de la aplicación en local.

##**Estructura del proyecto**##
Al tratarse de un proyecto en django, tenemos tres directorios principales:

* **Proyecto_Merka:** que contiene lo referente al proyecto.

* **merka:** que contiene los ficheros referentes a nuestra aplicación y que usa a su vez los del fichero "Proyecto_Merka"

* **templates/merka:** Contiene los templates que usa la aplicación merka. 

##**Instalación local de la aplicación**##

Tenemos que ejecutar lo siguiente:

```
git clone https://github.com/AngelValera/proyectoIV-Modulo-1.git
cd proyectoIV-Modulo-1
python manage.py migrate
python manage.py runserver
```


##**Desarrollo basado en pruebas**##
Para las pruebas, usamos el fichero **[test.py](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/merka/tests.py)** y para su ejecución usamos la herramienta manage.py :

**python manage.py test** ó **python manage.py test nombreaplicacion**

Estos test se usarán tanto en el despliegue en un Paas como en la integración continua.

##**Integración continua**##

Para la integración continua he utilizado travis, ya que es el que me ha resultado más sencillo de utilizar junto con github:


[Más Información](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Documentacion/IntCont.md)

##**Despliegue en un Paas Heroku**##

El siguiente paso es desplegar nuestra aplicación en un Paas, he utilizado heroku, lo he escogido porque aprendí a utilizarlo con los ejercicios del tema 3 y me resultó sencillo de usar, además de porque necesita un fichero de configuración que describe la infraestructura virtual.

La aplicación podemos verla funcionando [aquí](https://proyecto-merka.herokuapp.com/).

[Más Información](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Documentacion/PAAS.md)


##**Entorno de pruebas**##

Para el entorno de pruebas se ha utilizado Docker el cual está basado en un sistema de contenedores. Para su uso, he creado una imagen basada en Ubuntu la cual tiene la aplicación MerKa descargada y preparada para su ejecución y la cual puede ser obtenida con una sola orden desde DockerHub. [Imagen en DockerHub](https://hub.docker.com/r/angelvalera/proyectoiv-modulo-1/)

[Más Información](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Documentacion/docker.md)

##**MEJORAS**##
Este es un apartado para facilitar la corrección de la práctica, en el que se indican las mejoras que se han añadido a la aplicación en este nuevo hito.

[MEJORAS](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Documentacion/mejoras.md)