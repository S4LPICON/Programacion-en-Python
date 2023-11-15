"""
Calcular el n-esimo término de la serie de Fibonacci.

Para n = 7, la serie de Fibonacci es:  1, 1, 2, 3, 5, 8,13, por lo tanto, el séptimo término es 13 , la funcion debe llamarse calcular_nesimo_fibonacci(x)
"""
def calcular_nesimo_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print((calcular_nesimo_fibonacci(7)))