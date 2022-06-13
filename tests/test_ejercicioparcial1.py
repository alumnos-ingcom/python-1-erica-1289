################
#Erica Suarez- @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test de prueba del ejercicio 1 del parcial verificamos que el tipo de dato retornado
sea el esperado y que el resultado sea el correcto.
"""
from src.ejercicioparcial1 import multiplicacion

def multiplicacion():
    """
    Probamos la función multiplicacion.
    """
    suma = 0 
    contador = 0
    if numero_1  > 0:
        while contador < (numero_2):
            suma +=numero_1
            contador +=1

    return suma
numero_1 = int(input('Ingrese un valor: '))
numero_2 =int(input('Ingrese otro valor: '))
resultado=multiplicacion(numero_1, numero_2)
print(resultado)