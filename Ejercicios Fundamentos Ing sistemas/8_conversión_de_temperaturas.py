"""
Hacer una función por cada formula de conversión de temperaturas:

Centígrados  (C) a Fahrenheit (F)         F= C x (9 / 5) + 32
Fahrenheit (F)  a Centígrados (C)         C= (F-32) x (5 / 9 )
Centígrados a Kelvin(K)                       K =  C + 273.15
Kelvin(F) a Centígrados(C)                   C = K - 273.15

Ejemplos:
   centigrados_fahrenheit (10) retorna 50.0
   fahrenheit_centigrados (10) retorna -12.222222222222223
   centigrados_kelvin (10) retorna 283.15
  kelvin_centigrados (10) retorna -263.15
"""
def centigrados_fahrenheit(x):
    rta = x * (9 / 5) + 32
    return rta
def fahrenheit_centigrados(x):
    rta = (x-32) * (5 / 9 )
    return rta
def centigrados_kelvin(x):
    rta = x + 273.15
    return rta
def  kelvin_centigrados(x):
    rta = x - 273.15
    return rta