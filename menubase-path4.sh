#!/bin/bash

# Mostrar una lista de todos los archivos .sh en todas las carpetas y subcarpetas dentro del directorio ~/ (tu directorio de inicio)
echo "Archivos .sh en todas las carpetas y subcarpetas dentro del directorio ~/ (tu directorio de inicio):"
find ~/ -type f -name "*.sh" | more
echo

# Pedir al usuario que ingrese el nombre del archivo .sh que desea agregar al PATH
echo "Por favor, introduce el nombre del archivo .sh que deseas agregar al PATH:"
read filename

if [ -f "$filename" ] && [ "${filename: -3}" == ".sh" ]; then
  # Obtener el directorio donde se encuentra el script
  dir=$(dirname "$filename")

  # Agregar el directorio al PATH
  if [[ ":$PATH:" != *":$dir:"* ]]; then
    echo "Añadiendo '$dir' al PATH"
    export PATH="$PATH:$dir"
  else
    echo "'$dir' ya está en el PATH"
  fi
else
  echo "El archivo '$filename' no existe o no es un archivo .sh"
fi

# Este script utiliza el comando find para buscar archivos .sh en todas las carpetas y subcarpetas dentro del directorio ~/ (tu directorio de inicio) y luego muestra la salida en páginas utilizando el comando more.

# Recuerda dar permisos de ejecución al archivo con el comando chmod +x archivo.sh y ejecutar el script con ./archivo.sh.