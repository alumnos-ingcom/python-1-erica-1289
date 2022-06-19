################
# Erica Suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa. Esto quiere
decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

def suma_lenta(numero, otro_numero):
    
    suma = numero
    c=0
    if otro_numero  > 0:
        while c < (otro_numero):
            suma +=1
            c +=1
    else:
        while c < -1*(otro_numero):
            suma -=1
            c +=1
    return suma


def principal():
    """
    Esta función es la que se encarga de recibir 2 números enteros y realizar suma suma lenta.
    Precondición: Ingresar 2 números enteros.
    Poscondición: Como resultado obtendremos un número entero.
    
    Args:
        numero(int):
        otro_numero(int):
    return:
        REtorna la operación suma.
        
    """
    numero=int(input("Ingrese un número: "))
    otro_numero=int(input("Ingrese otro número: "))
    resultado = suma_lenta(numero,otro_numero)
    print(resultado)

if __name__ == "__main__":
    principal()
    
