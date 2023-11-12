"""
Hacer una función que dado un número de 3 cifras retorne el número invertido.

Ejemplos:     al llamado invertir(791) retornará 197
                     al llamado invertir(248) retornará 842
"""
def invertir(numero):
    numero_invertido = int(str(numero)[::-1])
    return numero_invertido