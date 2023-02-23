

import random

letras = "abcdefghijklmnnopgrstuvwxyzABCDEF"
numeros = "0123456789"
simbolos = "#0=<>([])?L-;)][])"

def generar_contrasena(longitud):
    caracteres = letras + numeros + simbolos
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
contrasena = generar_contrasena(longitud)

print("La contraseña generada es:", contrasena)

# Guardar la contraseña en un archivo
with open('contraseñas2.txt', 'a') as archivo:
    archivo.write(contrasena + '\n')

# En este ejemplo, la contraseña generada se guarda en un archivo llamado "contraseñas2.txt" utilizando la función open() en modo de apendizaje 'a'. La contraseña se escribe en una nueva línea del archivo cada vez que se guarda, para que cada contraseña quede en una línea separada.

# La sentencia with se usa para abrir y cerrar automáticamente el archivo, lo que garantiza que los datos se escriban correctamente en el archivo.

# Cada vez que se ejecute el programa, se agregará una nueva contraseña al final del archivo "contraseñas2.txt".










# import random

# letras = "abcdefghijklmnnopgrstuvwxyzABCDEF"
# numeros = "0123456789"
# simbolos = "#0=<>([])?L-;)][])"

# def generar_contrasena(longitud):
#     caracteres = letras + numeros + simbolos
#     contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
#     return contrasena

# longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
# contrasena = generar_contrasena(longitud)

# print("La contraseña generada es:", contrasena)

# # En este ejemplo, las variables de letras, números y símbolos se combinan en la variable caracteres y se utilizan para generar la contraseña utilizando la función generar_contrasena(). La longitud de la contraseña se solicita al usuario a través de la función input().

# # Como en el ejemplo anterior, puedes modificar el código para guardar las contraseñas generadas en un archivo utilizando la técnica descrita anteriormente.