"""
Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica cuando el sexo es femenino es:  num.pulsaciones = (220 - edad)/10  y si el sexo es masculino:  num.pulsaciones = (210 - edad)/10

La función se llama calcular_pulsaciones y recibe como parámetros la edad de la persona y el sexo de la persona
para sexo masculino calcular_pulsaciones(24,"m") y para femenino calcular_pulsaciones(20,"f")
"""
def calcular_pulsaciones(a, b):
    if b == "m":
        rta = (210 - a) / 10
    else:
        rta = (220 - a) / 10
    return rta