![resultado del test](https://travis-ci.org/AngelValera/proyectoIV-Modulo-1.svg?branch=master)
![snap-ci](https://snap-ci.com/AngelValera/proyectoIV-Modulo-1/branch/master/build_image)
## **Proyecto de infraestructura virtual junto con desarrollo de aplicaciones para Internet** ##

### **Hito 1: Merka** ###

### **Participantes:** ###

#### Ángel Valera Motos  ####
#### Bogdan Alin Muresan ####

**Descripción:**

Nuestra aplicación se trata de un sistema de gestión de paquetes, de modo que la aplicación web será una tienda online, desarrollada en python, en un framework de alto nivel como Django. Dicha tienda consistirá en que tu puedes comprar algún tipo de producto, realizar un seguimiento de dicho producto.

El proyecto se va a desarrollar en dos módulos, dentro de un repositorio principal de  tipo [organización](https://github.com/ProyectoIV-DAI/ProyectoIV-Modulo-Principal.git):

**El módulo 1:**  [(Ángel Valera Motos )](https://github.com/AngelValera/proyectoIV-Modulo-1.git)Este módulo se encarga de toda la gestión de las bases de datos necesarias. Al tratarse de una tienda online necesitaremos base de datos (MySQL) replicadas, una base de datos para usuarios, para productos, etc. 

Hemos elegido llevar a cabo este proyecto, porque se centra en la virtualización de recursos como puede ser el uso de máquinas virtuales para el despliegue de una aplicación para Internet, usando también para ello un framework de alto nivel.

Estamos inscritos en el certamen de proyectos de la UGR organizado por la OSL.

### **Hito 2: Merka** ###

##**Desarrollo basado en pruebas**##
He usado el framework Django, ya que decidimos hacer la aplicación en Python, por tanto usaremos las herramientas que proporciona, siendo estas manage.py y setup.py.

Para las pruebas, usamos el fichero [test.py](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/merka/tests.py) y para su ejecución usamos la herramienta manage.py :

**python manage.py test** ó **python manage.py test nombreaplicacion**

Estos test se usarán tanto en el despliegue en un Paas como en la integración continua.

##**Integración continua**##

Para la integración continua he utilizado travis, ya que es el que me ha resultado más sencillo d utilizar junto con github:

Para su uso debemos indicar el repositorio que queremos testear y además generar el fichero .travis.yml [.travis.yml](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/.travis.yml) donde se indican la versión de python usada, como instalar las dependencias y como pasar los test.

Para las dependencias se utiliza un fichero llamado [requirements.txt](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/requirements.txt) con lo necesario para ejecutar la aplicación.

Para generar la documentación, se utiliza la herramienta epydoc de la siguiente manera:

**epydoc --html views.py models.py**

Para ello debemos estar en el directorio de la aplicación, **merka**.

### **Hito 3: Merka** ###

##**Despliegue en un Paas Heroku**##

El siguiente paso es desplegar 






































