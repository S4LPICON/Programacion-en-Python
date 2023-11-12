""" 
Escribe una función con dos parámetros de tal forma que determine si sus dos parámetros son múltiplo el uno del otro (no importa cuál de cuál), esta función debe retornar true  si son múltiplos o false si no 

multiplos(3,6)
"""
def multiplos(a,b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False