#!/usr/bin/python3
"""El módulo Calculadora tiene como finalidad brindar operaciones
aritméticas. (suma, resta, multiplicación, división)
"""
#METADATAS
__author__ = "Daniel Eduardo Ramos Mencía"
__copyright__ = "Copyright 2022, DERM DEVS"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "danieldermramos@gmail.com"
__status__ = "Developer"

def suma(x, y):
    """Recibe dos numeros y retorna la suma de estos"""
    s = x + y
    return s

def resta(x, y):
    """Recibe dos numeros y retorna la resta de estos"""
    r = x - y
    return r

def producto(x, y):
    """Recibe dos numeros y retorna el producto de estos"""
    p = x * y
    return p

def division(x, y):
    """Recibe dos numeros y retorna la division de estos"""
    if y != 0:
        d = x / y
    else:
        d = None
        print("No se puede dividir entre 0")
    return d
