"""
 Dado un número X de 3 cifras determine la suma de las cifras pares

Ejemplo: Si el número de tres cifras es 364, de los tres dígitos, los pares son 6 y 4 por lo tanto la Suma de sus dígitos pares es 10

sumar_cifras_pares(247) la funcion recibe como parametros un numero entero y en este caso retornaria 6 ya que 2+4=6
"""
def sumar_cifras_pares(numero):
    if 100 <= numero <= 999:
        cifra_hundreds = numero // 100
        cifra_tens = (numero % 100) // 10
        cifra_ones = numero % 10
        suma_pares = 0
        if cifra_hundreds % 2 == 0:
            suma_pares += cifra_hundreds
        if cifra_tens % 2 == 0:
            suma_pares += cifra_tens
        if cifra_ones % 2 == 0:
            suma_pares += cifra_ones

        return suma_pares
    else:
        return "El número debe ser de tres cifras."