# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    if n <= 0:
        return 0
    suma = 0
    for number in range(1, n + 1):
        suma += number
    return suma
def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
    if n <= 0:
        return 0
    suma = 0
    for par in range(1, n +1):
        if par % 2 == 0:
            suma += par
    return suma


def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """
    if n <= 0:
        return 1
    suma = 1
    for num in range(1, n + 1):
        suma = num * suma
    return suma
