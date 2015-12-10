#!/bin/bash

#Descarga docker
sudo apt-get update
sudo apt-get install -y docker.io
# Inicia el servicio docker
sudo service docker start
sudo docker -d &
#Descarga la imagen
sudo docker pull angelvalera/proyectoiv-modulo-1
#Ejecuta la imagen
sudo docker run -i -t angelvalera/proyectoiv-modulo-1 /bin/bash
