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
        Tuple: Tupla que contiene todos los números primos encontrados.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """
    Descompone un número en sus factores primos.

    Argumentos:
        numero (int): Número a descomponer en factores primos.

    Retorna:
        Tuple: Tupla que contiene los factores primos del número, incluidos los repetidos.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)

def contar_factores(factores):
    """
    Cuenta la cantidad de veces que aparece cada factor primo en la tupla.

    Argumentos:
        factores (Tuple[int, ...]): Tupla de factores primos.

    Retorna:
        Dict[int, int]: Diccionario con factores primos como claves y su frecuencia como valores.
    """
    conteo = {}
    for factor in factores:
        conteo[factor] = conteo.get(factor, 0) + 1
    return conteo

def mcm(numero1, numero2):
    """
    Calcula el mínimo común múltiplo de dos números.

    Argumentos:
        numero1 (int): Primer número.
        numero2 (int): Segundo número.

    Retorna:
        int: El mínimo común múltiplo de los números dados.

    >>> mcm(90, 14)
    630
    """
    factores1 = contar_factores(descompon(numero1))
    factores2 = contar_factores(descompon(numero2))

    factores_mcm = {factor: max(factores1.get(factor, 0), factores2.get(factor, 0))
                    for factor in set(factores1).union(factores2)}

    resultado = 1
    for factor, exponente in factores_mcm.items():
        resultado *= factor ** exponente

    return resultado

def mcd(numero1, numero2):
    """
    Calcula el máximo común divisor de dos números.

    Argumentos:
        numero1 (int): Primer número.
        numero2 (int): Segundo número.

    Retorna:
        int: El máximo común divisor de los números dados.

    >>> mcd(924, 780)
    12
    """
    factores1 = contar_factores(descompon(numero1))
    factores2 = contar_factores(descompon(numero2))

    factores_mcd = {factor: min(factores1[factor], factores2[factor])
                    for factor in set(factores1).intersection(factores2)}

    resultado = 1
    for factor, exponente in factores_mcd.items():
        resultado *= factor ** exponente

    return resultado

def mcmN(*numeros):
    """
    Calcula el mínimo común múltiplo de múltiples números.

    Argumentos:
        *numeros (int): Números a evaluar.

    Retorna:
        int: El mínimo común múltiplo de todos los números proporcionados.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    return reduce(mcm, numeros)


def mcdN(*numeros):
    """
    Calcula el máximo común divisor de múltiples números.

    Argumentos:
        *numeros (int): Números a evaluar.

    Retorna:
        int: El máximo común divisor de todos los números proporcionados.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    return reduce(mcd, numeros)

if __name__ == "__main__":
    doctest.testmod(verbose=True)
