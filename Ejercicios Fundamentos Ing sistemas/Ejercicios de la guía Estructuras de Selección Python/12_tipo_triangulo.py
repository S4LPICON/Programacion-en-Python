"""
Dada las longitudes de los lados de un triángulo, hacer una función que determine el tipo de triangulo, teniendo en cuenta la siguiente clasificación:

Si los tres lados son iguales es equilátero

Si solo dos lados son iguales isósceles

Si todos son diferentes escalenos

tipo_triangulo(6,6,6) esta funcion recibe como parámetros 3 números enteros cada uno es la la longitud de cada lado del triangulo y retornara el tipo de triangulo "equilatero" , "isosceles","escaleno"
"""
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "equilatero"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "escaleno"
