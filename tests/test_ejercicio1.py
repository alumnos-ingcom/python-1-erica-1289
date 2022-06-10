################
# Erica Suarez - @erica-1289
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
test de prueba del ejercicio 1 verificamos que el tipo de dato retornado
sea el esperado y que el resultado sea el correcto
"""
from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados


def test_convertir_a_fahrenheit():
    """
       probamos la funcion de conversion a fahrenheit
    """
    valor = 0
    resultado = convertir_a_fahrrenheit(valor)
    assert isinstance(resultado, float), "no es del tipo esperado"
    assert resultado == 32, "no es el valor esperado"


def test_convertir_a_centigrados():
    """
       probamos la funcion de conversion a centigrados
    """
    valor = 32
    resultado = convertir_a_centigrados(valor)
    assert isinstance(resultado, float), "no es del tipo esperado"
    assert resultado == 0, "no es el valor esperado"
