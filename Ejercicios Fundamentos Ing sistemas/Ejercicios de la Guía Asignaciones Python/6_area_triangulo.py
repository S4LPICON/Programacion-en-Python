"""
Calcular el área de un triángulo en función de las longitudes de sus lados p(p−a)(p−b)(p−c)−−−−−−−−−−−−−−−−−√2
  donde p es el semiperímetro p=(a+b+c)/2 . Averigüe la función que dispone el lenguaje para calcular una raíz cuadrada. Nota: No toda combinación de valores de a, b y c forman un triángulo, para probar es necesario garantizar que cada lado sea menor que la suma de los otros dos por ejemplo 3, 4 y 5

ejemplos:   area_triangulo(7.8, 6, 3) retorna 8.081979955431718
                  area_triangulo(4, 4 , 2)  retorna   3.872983346207417
"""
import math

def area_triangulo(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    return area