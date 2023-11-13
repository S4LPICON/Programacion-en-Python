"""
Un empleado trabajar 40 horas semanales en una empresa y recibe un salario de 260.000 pesos semanales. Si excede de las 40 horas la empresa debe pagar un recargo del 30% por hora extra trabajada. Hacer una función que, dadas las horas semanales trabajadas de un empleado, retorne el salario a pagar según estas condiciones.

ejemplo: sueldo_horas_trabajadas(50) retorna 344500.0
"""
def sueldo_horas_trabajadas(horas_trabajadas):
    salario_base = 260000 
    horas_normales = 40 
    tarifa_hora_extra = 1.3  

    if horas_trabajadas <= horas_normales:
        salario_total = salario_base
    else:
        horas_extra = horas_trabajadas - horas_normales
        salario_total = salario_base + (horas_extra * tarifa_hora_extra * (salario_base / horas_normales))

    return salario_total