import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
contrasena = generar_contrasena(longitud)

print("La contraseña generada es:", contrasena)


# Este programa utiliza las bibliotecas integradas de Python random y string. La función generar_contrasena() toma un argumento de longitud que se utiliza para definir la longitud de la contraseña que se generará.

# La variable caracteres contiene una cadena de todos los caracteres posibles que se utilizarán para generar la contraseña. Esta cadena incluye letras mayúsculas y minúsculas, dígitos y caracteres especiales.

# La función join() toma una lista de caracteres aleatorios generados por random.choice() y los une en una cadena única.

# Finalmente, la contraseña generada se imprime en la pantalla.

# Puedes personalizar la lista de caracteres utilizados para generar la contraseña ajustando la variable caracteres. Además, puedes envolver la llamada a la función generar_contrasena() en un ciclo while para generar varias contraseñas seguras de forma automática.
