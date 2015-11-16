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

El siguiente paso es desplegar nuestra aplicación en un Paas, he utilizado heroku, lo he escogido porque aprendí a utilizarlo con los ejercicios del tema 3 y me resultó sencillo de usar, además de porque necesita un fichero de configuración que describe la infraestructura virtual.

Por tanto los ficheros que necesitamos para el despliegue son:

- **Procfile:** se usa para que heroku sepa que tiene que ejecutar, para ello utiliza gunicorn:

```
web: gunicorn Proyecto_Merka.wsgi --log-file -
```
- **requirements.txt**: Como ya indiqué anteriormente para que la aplicación funcione necesita indicar que necesita para ejecutarse:

Una vez definidos estos ficheros debemos desplegarla en heroku, para ello hay que realizar una serie de comandos:

Lo primero es clonarnos el repositorio de github de la aplicación (si no lo teniamos ya clonado) y acontinuación:

**wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh**

**heroku login**-->Nos logueamos dentro de heroku

**heroku create**-->Creamos la aplicación dentro deheroku

**heroku apps:rename merka**-->Le cambiamos el nombre que nos pone por defecto por el de merka

**git push heroku master**-->La desplegamos.

En cuanto a la base de datos estoy usando la base de datos Postgre que nos proporciona Heroku, en local sigo usando SQLite, para ello :

1- Instalar psycopg2.

2- Instalar dj_database_url.

3- Ahora en el fichero setting.py debemos añadir lo siguiente para poder usar SQLite en local y Postgree en Heroku:

```python

import dj_database_url

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
    DATABASE_URL='postgres://wbjycrkkhvpsgd:lNgVyf_dKRgVJ3mRAumWxSXwp1@ec2-54-204-7-145.compute-1.amazonaws.com:5432/d9adsr028lbovr'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
```
4- En el fichero  wsgi.py debemos añadir también las siguientes líenas:

```python
from dj_static import Cling

application = Cling(get_wsgi_application())
```

Ahora debemos subir cambios a github y hacer git push heroku master y crear las tablas dentro de la base de datos para ello tenemos que introducir:

**1- heroku run python manage.py makemigrations**

**2- heroku run python manage.py migrate**

**3- heroku run python manage.py createsuperuser**


Hecho esto, ya tenemos la aplicación desplegada, podemos verla en este [enlace](https://proyecto-merka.herokuapp.com/):


Ahora añadimos integracion continua con Snap-ci, para ello seleccionamos el repositorio que queremos y lo configuramos de la siguiente manera:

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_001_zpsfxmmbpla.png)

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_003_zpsi4nfpcv3.png)

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_022_zpsu3ksskro.png)

con esto cada vez que hagamos push  nos pasará los test y si son satisfactorios desplegará la aplicación.












