################
# Erica suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique
si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""
# Reemplazar por las funciones del ejercicio


def signo(numero):
    """
    Esta función es la que se encarga de mostrar si un número es positivo, negativo o cero,
    
    
    Args:
        numero(float): Este es el número a evaluar si es positivo, negativo o cero.
        
    """
    
    
    if (numero + numero < numero):
        print(numero, "es un número negativo.")
    elif numero + numero > numero:
        print(numero, "es un número positivo.")
    else:
        print(numero, 'es cero.')
        
num=float(input("Ingrese el número a evaluar: "))
print(signo(num))    



if __name__ == "__main__":
    signo()
    
    
  