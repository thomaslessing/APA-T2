"""

Thomas Lessing

Este módulo proporciona funciones para el manejo de números primos, incluyendo:

- Determinación de la primalidad de un número.
- Obtención de números primos menores que un número dado.
- Descomposición en factores primos.
- Cálculo del mínimo común múltiplo (MCM).
- Cálculo del máximo común divisor (MCD).
- Obtención del MCM y MCD para múltiples números.
- Pruebas unitarias para verificar la correcta implementación de las funciones.

"""
import doctest
def esPrimo(numero):
    """"
    Devuelve true si el numero es primo, false si no lo es
    
    >>> for numero in range(2, 10):
    ...    print(esPrimo(numero))
    True
    True
    False
    True
    False
    True
    False
    False
    
    """
    
    for prueba in range(2, numero):
        if numero % prueba == 0: return False

    return True 

def primos(numero):
    """
    Genera una tupla con todos los números primos menores al número proporcionado.

    Argumentos:
        numero (int): Límite superior para buscar números primos (no incluido).

    Retorna:
        Tuple[int, ...]: Tupla que contiene todos los números primos encontrados.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))




