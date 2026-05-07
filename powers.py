# Replace the "ANSWER HERE" for your answer

def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
    if exp == 0:
        return 1
    suma = 1
    for potencia in range(exp):
        suma *= base
    return suma




def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    total_suma = 0
    for max in range(max_exp + 1):
        total_suma += power(base, max)
    return total_suma
    
