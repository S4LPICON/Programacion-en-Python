"""
Dados dos (2) números ·”x” y “z” donde “x” es menor que “z” haga una función para calcular la suma de los números comprendidos entre” x” y “z”.

El nombre de la función debería ser suma_comprendida(x,z) , ejemplo al llamado de la funcion  suma_comprendida(2,6) con los valores de 2 y 6 retornará como resultado la suma de 2+3+4+5+6 = 20
"""

def suma_comprendida(x,z):
    rta = 0
    if x<=z:
        while x <= z:
            rta = rta + x
            x = x + 1
    else:
        rta = 0
    return rta

print(suma_comprendida(-10,-10))