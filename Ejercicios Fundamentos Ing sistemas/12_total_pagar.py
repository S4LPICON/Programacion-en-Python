"""
Un vendedor recibe un sueldo base mensual, más un 10% de las ventas realizadas (comisión), hacer una función llamada total_pagar que dado el salario base y el total de ventas realizadas retorne el salario que le corresponde en el mes.

Ejemplo:

   total_pagar(300000, 5000000)  retorna 800000.0
"""
def total_pagar(sala_base,to_ventas):
    rta= sala_base + to_ventas * 0.10
    return rta
