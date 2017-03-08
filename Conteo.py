#Funcion para calcular el factorial de un numero#

def factorial(n):
    """Permutaciones"""

    factorial = 1

    while (n > 1):
        factorial = factorial * n
        n-=1

    return factorial


def permutacionesRep(n,divisiones):
    """Permutaciones con repeticion"""

    resultadoDivisiones = 1

    for numero in divisiones:
        resultadoDivisiones = resultadoDivisiones * numero

    permutacionesR = factorial(n) / resultadoDivisiones

    return permutacionesR


def variaciones(n,c):
    """Variacion de n numeros en tuplas de c numeros, sin repetir numeros"""

    variacion = factorial(n) / factorial(n - c)
    return variacion


def variacionesRep(n,c):
    """Variaciones de n numeros en tuplas de c, con repeticiones"""

    variacionR = n ** c
    return variacionR