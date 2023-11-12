"""
 Calcular el valor absoluto de un número real, sin usar funciones predefinidas del lenguaje.


Ejemplo:  valor_absoluto(10) retornará 1 
                valor_absoluto(-5) retornará 5
"""
def valor_absoluto(x):
    if x < 0:
        rta = x * -1
    else:
        rta = x
    return rta
