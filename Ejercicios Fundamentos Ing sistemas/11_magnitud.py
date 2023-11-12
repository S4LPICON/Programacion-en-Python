"""
Escriba una función llamada magnitud que tenga cuatro parámetros de entrada llamados x1, y1, x2, y2 y que retorne como resultado la distancia entre dos puntos cuyas coordenadas son (x1, y1) y (x2, y2) según la siguiente fórmula:

dist=(y2−y1)2+(x2−x1)2−−−−−−−−−−−−−−−−−−√2

Ejemplo  magnitud (1, 2 ,3 ,2 ) retorna 2
               magnitud (7, 3, 2 ,5) retorna 5.385164807134504
"""
import math
def magnitud(x1,y1,x2,y2):
    rta = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return rta
    
