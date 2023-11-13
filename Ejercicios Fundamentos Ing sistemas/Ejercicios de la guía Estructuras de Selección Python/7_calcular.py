"""
Escribe una función que tome 3 parámetros: dos de tipo real y uno de tipo carácter. La función deberá sumar, restar, multiplicar o dividir los valores de los dos primeros parámetros dependiendo del símbolo indicado en el tercer parámetro, y devolver el resultado (el carácter será ‘+’, ‘-‘, ‘ * ’, y ‘/ ’).

calcular(10,10,"+")

calcular(6,3,"-")

calcular(5,5,"*")

calcular(8,2,"/")
"""
def calcular(a, b, c):
    if c == "+":
        rta = a + b
    elif c == "-":
        rta = a - b
    elif c == "*":
        rta = a * b
    elif c == "/":
        if b != 0:
            rta = a / b
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Operación no válida: Utiliza '+', '-', '*' o '/'"
    return rta