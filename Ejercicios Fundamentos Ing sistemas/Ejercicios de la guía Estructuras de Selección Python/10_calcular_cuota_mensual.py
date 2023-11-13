"""
Calcular mediante una función el valor de la cuota mensual y mediante otra función el número de cuotas a pagar, por la realización de un préstamo en un banco con las siguientes condiciones: 

Si el préstamo es menor de $500000 se paga un interés de 10% sobre el total del préstamo y las cuotas mensuales quedan de un 3% del monto total. Si el préstamo está entre $500000 y $1000000 (inclusive) se paga un interés del 7% y las cuotas quedan de un 5% del monto total. 
Y si el préstamo es superior a $1000000 se paga un interés del 4% y las cuotas quedan de un 7% del monto total.

calcular_cuota_mensual(500000)
calcular_num_cuotas(500000) 
"""

def calcular_cuota_mensual(x):
    if x <= 500000:
        f = x * 1.10
        cuota = f * 0.03
    elif x <= 1000000:
        f = x * 1.07
        cuota = f * 0.05
    else:
        f = x * 1.04
        cuota = f * 0.07
    return str(int(cuota)) + ".0"
def calcular_num_cuotas(x):
    if x <= 500000:
        f = x * 1.10
        s = f * 0.03
        num_cu = f // s
    elif x <= 1000000:
        f = x * 1.07
        s = f * 0.05
        num_cu = f // s
    else:
        f = x * 1.04
        s = f * 0.07
        num_cu = f // s
    return num_cu
print(calcular_num_cuotas(500001))