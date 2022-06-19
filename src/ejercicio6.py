################
# Erica Suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables
de tipo entero retorne una tupla con dichos valores
ordenados de menor a mayor y viceversa.
"""

def ordenar_mayor_a_menor(uno, dos, tres):# Reemplazar por las funciones del ejercicio
    
    if (tres < dos and dos < uno):
        print(uno, dos, tres)

    elif (dos < uno and uno < tres):
        print(tres, uno, dos)

    else:
        print(tres, dos, uno)
        
def ordenar_menor_a_mayor(uno, dos, tres):
    if (tres > dos and dos > uno):
        print(uno, dos, tres)
        
    elif (dos > uno and uno > tres):
        print(tres, uno, dos)
        
    else:
        print(dos, uno, tres)
        

def principal():
    
    #def ordenar_mayor_a_menor(uno, dos, tres)
    """
    Esta función es la que se encarga de ordenar
    los valores de mayor a menor.
    
    
    Args:
        uno(int): Es uno de los valores a comparar
        dos(int): Es otro de los valores a comparar.
        tres(int): Es le tercer valor a comprar.
        
    """
    #def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función es la que se encarga de ordenar los valores
    de menor a mayor.
    
    
    Args:
        uno(int): Es uno de los valores a comparar
        dos(int): Es otro de los valores a comparar.
        tres(int): Es le tercer valor a comprar.
    
    
    """
    
    uno = int(input("Ingrese un valor: "))
    dos = int(input("ingrese el segundo valor: "))
    tres = int(input("Ingrese el tercer valor: "))

    ordenar_mayor_a_menor(uno, dos, tres)
    ordenar_menor_a_mayor(uno, dos, tres)

if __name__ == "__main__":
    principal()