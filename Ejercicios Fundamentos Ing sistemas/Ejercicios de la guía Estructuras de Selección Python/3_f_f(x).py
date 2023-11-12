"""
Calcular f def (x) donde f es una función de los reales en los reales, definida por

        x si x<-5
f(x) =  x+3 si -5 <= x <=5
        x**2 si x>5

Ejemplo al llamado de 
           calcular_f(-6) retornará -6
           calcular_f(-5) retornará -2
           calcular_f(5) retornará 8
           calcular_f(1) retornará 4
           calcular_f(6) retornará 34
"""

def calcular_f(x):
    if x<-5:
        rta = x
    else:
        if -5 <= x <=5:
            rta = x + 3
        else:
            rta = x**2 -2
    return rta