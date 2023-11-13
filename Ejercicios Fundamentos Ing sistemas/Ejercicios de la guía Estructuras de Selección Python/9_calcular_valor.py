"""
Un café Internet cobra a sus usuarios de la siguiente forma.

tiempo de navegacion       valor a pagar
de 1 a 15 minutos           500
de 16 a 30 minutos          1000
de 31 a 60 minutos          1400


Superior a 60 minutos, 20 pesos el minuto adicional.

Hacer una función que dado el tiempo navegado por una persona (en minutos) determinar y retorne el valor a pagar

calcular_valor(15) retorna 500 extras
"""
def calcular_valor(x):
    if x <= 15:
        rta = 500
    elif x > 15 and x<=30:
        rta = 1000
    elif x > 30 and x <=60: 
        rta = 1400
    else:
        rta = 1400 + ((x -60) *20)
    return rta