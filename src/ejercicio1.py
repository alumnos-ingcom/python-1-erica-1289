################
# Erica Suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados
centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados
centigrados en fahrenheit como un número decimal, utilice esta
formula para calcular los grados centígrados y retorne el resultado
obtenido. Y viceversa.
"""
def convertir_a_fahrrenheit(centigrados):
    """convertir_a_fahrrenheit(int|float)->float
    esta funcion recibe un valor y devuelve su equivalente en grados
    fahrenheit
    """
    fahrenheit=(centigrados*1.8)+32
    return fahrenheit


def convertir_a_centigrados(fahrenheit):
    centigrados=(fahrenheit - 32) * 5 / 9 
    return centigrados


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    centigrados=float(input("Ingrese los grados: "))
    fahrenheit=float(input("Ingrese los grados: "))
    print(convertir_a_fahrrenheit(centigrados))
    print(convertir_a_centigrados(fahrenheit))

if __name__ == "__main__":
    principal()

