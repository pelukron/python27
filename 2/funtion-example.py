import math


def funcion_factorial(numero):
    ''' Regresar el factorial de un numero.
    https://www.geeksforgeeks.org/factorial-in-python/

    Parameters:
        numero (int): valor que determina el numero de veces que se multiplicara

    Returns:
        factorial(int): valor a regresar multiplicado @numero veces
    '''
    factorial = 1
    i = 1
    for i in range(i, numero+1):
        factorial = factorial * i
    return factorial


def funcion_factorial_marth(numero):
    return math.factorial(numero)


print("function factorial a mano", funcion_factorial(20))

print("function factorail con math", funcion_factorial_marth(20))
