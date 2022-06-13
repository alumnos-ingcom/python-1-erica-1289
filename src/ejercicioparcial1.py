################
# Erica Suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1: Matematica lenta III
Ambas funciones deben implementar las operaciones pedidas con
sumas y restas, además de considerar números enteros positivos y negativos
tanto para los argumentos como para los resultados. Sin utilizar lazos for,
range y los operadores tradicionales.
"""
# Reemplazar por las funciones del ejercicio


def multiplicacion(numero_1, numero_2):
    """
    Esta función es la que se encarga de la dar el resultado de la multiplicacion realizad
    por suma y resta lenta.
    
    
    Argms:
        numero_1(int):Es el valor contador.
        numero_2(int9: Es el valor a multiplicar.
    
    Returns:
        Retorno la variable suma
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


if __name__ == "__main__":
    multiplicacion(numero_1, numero_2)