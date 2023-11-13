"""
hacer la funcion factorial
"""
def factorial(x):
    i=1
    rta=1
    if x > 0:
        while i <=x:
            rta = rta * i
            i = i+1
    else:
        rta = 1
    return rta

print(factorial(0))