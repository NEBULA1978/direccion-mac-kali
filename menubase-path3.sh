#!/bin/bash

# Mostrar una lista de todos los archivos .sh en las carpetas de nivel superior dentro del directorio ~/ (tu directorio de inicio)
echo "Archivos .sh en las carpetas de nivel superior del directorio ~/ (tu directorio de inicio):"
find ~/ -maxdepth 1 -type d -exec sh -c 'printf "\n%s:\n" "$0"; find "$0" -maxdepth 1 -name "*.sh" -type f -printf "  %p\n"' {} \;
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

# Este script utiliza el comando find para buscar carpetas de nivel superior dentro del directorio ~/ (tu directorio de inicio) y luego busca archivos .sh dentro de esas carpetas. Luego, muestra una lista de todos los archivos encontrados.

# Recuerda dar permisos de ejecución al archivo con el comando chmod +x archivo.sh y ejecutar el script con ./archivo.sh.