import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
contrasena = generar_contrasena(longitud)

print("La contraseña generada es:", contrasena)

# Guardar la contraseña en un archivo
with open('contrasenas.txt', 'a') as archivo:
    archivo.write(contrasena + '\n')

# En este ejemplo, la contraseña generada se guarda en un archivo llamado "contrasenas.txt" utilizando la función open() en modo de apendizaje 'a'. La contraseña se escribe en una nueva línea del archivo cada vez que se guarda, para que cada contraseña quede en una línea separada.

# La sentencia with se usa para abrir y cerrar automáticamente el archivo, lo que garantiza que los datos se escriban correctamente en el archivo.

# Cada vez que se ejecute el programa, se agregará una nueva contraseña al final del archivo "contrasenas.txt". Si deseas que el archivo tenga un nombre diferente, solo cambia el nombre en la función open().
