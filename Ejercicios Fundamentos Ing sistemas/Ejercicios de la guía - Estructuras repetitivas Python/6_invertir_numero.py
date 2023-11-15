"""
Dado un número natural n (de cualquier cantidad de dígitos) hacer una función que encuentre otro entero m que sea n al revés, invirtiendo el orden de los dígitos y otra función que permita saber si n es un palíndromo. Si n es un palíndromo, entonces se lee igual de izquierda a derecha que de derecha a izquierda. Ejemplos: para n=345 el n al revés es 543 y no es palíndromo. Para n=75357 el n al revés es 75357 y por lo tanto si es palíndromo.

El nombre de las funciones serian invertir_numero(x) y palindromo(x) , la funcion invertir devuelve el numero invertido y la funcion palindromo devuelve True o False 
"""

def invertir_numero(n):
    numero_invertido = int(str(n)[::-1])
    return numero_invertido

def palindromo(n):
    numero_str = str(n)
    return numero_str == numero_str[::-1]