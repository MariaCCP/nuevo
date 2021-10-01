# Descargar la libreria de SymPy
from sympy import isprime, primerange
x = int(input("Poner un numero: "))


def isPosible(n):
    for i in primerange(2, n):
        x = n - i
        if isprime(x):
            return f"{i} {x}"
    return "No se puede"


print(isPosible(x))