"""
Juan Pablo Montoya, entrena todos los días, recorriendo cierta cantidad de kilómetros, de tal forma que todos los días recorre el doble de lo que recorrió el día anterior más 10 km. Pero cada 3 días recorre solo la mitad de lo que recorrió el día anterior. Realice una función que dado el número de kilómetros recorridos el primer día del entrenamiento y un número n de días y halle el total de kilómetros acumulados hasta ese día (el n-ésimo día).

Por ejemplo, si el primer día recorrió 5 Km tenemos la siguiente tabla 

Día    Kms Recorridos       Acumulado

1               5               5  

2     5*2)+10  =   20           25  

3     20/2   =     10           35  

4     (10*2)+10 =  30           65  

5     (30*2)+10 =  70           135 

6      70/2   =    35           170

7     (35*2) +10 = 80           250

 
la función debe llamarse calcular_kilometros_acumulados(x,d) 
donde x viene siendo la cantidad de kilómetros que debe recorrer el primer día y d 
el numero de días del entrenamiento según condiciones descritas, por lo que debe retornar la cantidad de kilometros acumulados en dicho entrenamiento.
"""

def calcular_kilometros_acumulados(kmi,nd):
    acomulado = kmi
    ayer = kmi
    dia = 2
    while (dia <=nd):
        if (dia % 3 ==0):
            hoy = ayer/2
        else:
            hoy = ayer*2+10
            acomulado = acomulado + hoy
            ayer = hoy
            dia = dia + 1
    return acomulado

print((calcular_kilometros_acumulados(20,12)))