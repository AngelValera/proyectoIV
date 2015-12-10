##**Despliegue en un Paas Heroku**##
El siguiente paso es desplegar nuestra aplicación en un Paas, he utilizado heroku, lo he escogido porque aprendí a utilizarlo con los ejercicios del tema 3 y me resultó sencillo de usar, además de porque necesita un fichero de configuración que describe la infraestructura virtual.

La aplicación podemos verla funcionando [aquí](https://proyecto-merka.herokuapp.com/).

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

