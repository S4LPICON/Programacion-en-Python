"""
1- Hacer dos funciones una para hallar el cociente y otra para hallar el residuo de una división entera de enteros positivos, mediante restas sucesivas (sin usar el operador “div” ni “mod” que disponen la mayoría de lenguajes de programación) …

Para el cálculo del cociente y del residuo de una división entera, usando restas sucesivas tenga en cuenta los siguientes ejemplos:

División entera entre 10 y 4

División entera entre 19 y 5

División entera entra 31 y 7

10 – 4 = 6
6 – 4   = 2

19   -  5  =   14
14   -  5  =   9
 9  -  5 =  4

31 -  7  =  24
24  -  7  =  17
17  -  7  =   10
10   -  7   =  3

Cociente 2 pues se hicieron dos restas

El residuo es 2 puesto que es el último resultado de la resta

El cociente es 3 pues se hicieron tres restas

El residuo es 4 puesto que es el último resultado de la resta

Cociente es 4

Residuo es 3

 Las funciones se deben nombrar cociente_division_entera(x,y) residuo_division_entera(x,y)
"""

def cociente_division_entera(x, y):
    cociente = 0
    while x >= y:
        x -= y
        cociente += 1
    return cociente

def residuo_division_entera(x, y):
    while x >= y:
        x -= y
    return x

print(cociente_division_entera(10, 4))