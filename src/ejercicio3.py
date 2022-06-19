################
# Erica Suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números.
Escribir una función que utilizando sumas y restas, recibir dos valores y devolver:

Retornar -1 si el primero es menor que el segundo.
Retornar 0 si son iguales.
Retornar 1 si el primero es mayor que el segundo.
"""
def compara(numero, otro_numero):# Reemplazar por las funciones del ejercicio

    suma = numero + otro_numero
    resta = numero - otro_numero
    return suma, resta


def principal():
    """
    Esta función es la que se encarga de comparar los resultados de las operaciones.
    precondición: Ingresar 2 números enteros.
    Poscondición: El resultado es un número entero. 
        
        
    Args:
        numero(float):es el primer digito que se toma para obtern el resultado de la suma y resta.
        otro_numero(float): esel segundonumero paraonterner el resultado de la suma y resta.
            
    Returns:
        Retorna -1 si el resultado de la suma es menor que el de la resta.
        Retorna 0 sí el resultado de la suma y de la resta son iguales.
        Retorna 1 sí el resultado de la suma es mayor que el de la resta.
        
    """
    numero = int(input("Ingrese un número: "))
    otro_numero = int(input("Ingrese un número: "))
    suma, resta = compara(numero, otro_numero)
    if suma  < resta:
        print("-1")
    elif suma == resta:
        print("0")
    else:
        print("1")
        

if __name__ == "__main__":
    principal()