"""
Realizar dos funciones que encuentren el número mayor y la otra 
el número menor de 3 números dados como parámetros a la respectiva función de tal forma que  
mayor(3,7,9) retornará 9  y menor(7,9,3) retornará 3
"""
def mayor(a,b,c):
    if a > b:
        if a>c:
            rta = a
        else:
            rta = c
    else:
        if b > c:
            rta = b
        else:
            rta = c
    return rta
def menor(a,b,c):
    if a < b:
        if a<c:
            rta = a
        else:
            rta = c
    else:
        rta = b
    return rta