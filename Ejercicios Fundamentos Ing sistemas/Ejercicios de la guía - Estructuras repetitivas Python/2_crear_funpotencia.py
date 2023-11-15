"""
Cree la función Potencia 


el nombre de la función debe ser potencia(2,3) donde el primer parámetro es la base y el segundo el exponente 
"""
def potencia(x,y):
    i = 1
    rta = x
    if x == 0 and y != 0:
        rta = 0
    elif x != 0 and y == 0:
        rta = 1
    elif y > 0:
        while i < y:
            rta = rta * x
            i = i+1
    elif y < 0:
        rta = 1/(x**(-y))
    else: 
        rta = "no definido"
    return rta

print(potencia(-5,-2))
