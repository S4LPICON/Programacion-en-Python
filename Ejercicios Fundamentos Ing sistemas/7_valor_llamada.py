"""
Determinar el valor de una llamada telefónica, si por los primeros 3 minutos se cobran 300 pesos   y 150 por cada minuto adicional

Suponer que las llamadas siempre duran 3 o más de 3 minutos. 

Ejemplo: valor_llamada(6), retornará 750
"""
def valor_llamada(x):
    if x > 3:
        rta = (x - 3) * 150 + 300
    else:
        rta = 300
    return rta