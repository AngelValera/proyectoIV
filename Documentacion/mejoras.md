##**Mejoras realizados en este último hito**##

* Reorganización del archivo README, para ello se crea la carpeta [documentación](https://github.com/AngelValera/proyectoIV-Modulo-1/tree/master/Documentacion) como apoyo de dicho archivo.

* Utilización de PostgreSQL en Heroku.

* Se crea una imagen de un sistema Ubuntu conteniendo la aplicación en [DockerHub](https://hub.docker.com/r/angelvalera/proyectoiv-modulo-1/).

* Se añade un script que permite desplegar la aplicación en Heroku, [heroku.sh](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Scripts/heroku.sh).

* Se añade un script que permite arrancar la aplicación en local, [ejecutar_App.sh](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Scripts/ejecutar_App.sh).

* Se añade a la aplicación secciones de productos y articulos a esos productos, que están en la base de datos.

* Se añaden nuevos [test](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/merka/tests.py) para comprobar la creación de nuevos productos y secciones, así como la comprobación de que lo que muestra el template index.html con secciones y sin secciones es correcto.

* Se añade un script que permite instalar Docker, descargar y lanzar la imagen de la aplicación,[docker.sh](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Scripts/docker.sh).