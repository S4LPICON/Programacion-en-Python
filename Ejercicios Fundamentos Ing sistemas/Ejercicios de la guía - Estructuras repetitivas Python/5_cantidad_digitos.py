"""
Hallar la cantidad de dígitos que tiene un número entero positivo o negativo

 ejemplo : cantidad_digitos(345) la respuesta seria 3
"""

def cantidad_digitos(x):
    k = str(abs(x))
    rta = 0
    for s in k:
        rta += 1
    
    return rta

print(cantidad_digitos(345))