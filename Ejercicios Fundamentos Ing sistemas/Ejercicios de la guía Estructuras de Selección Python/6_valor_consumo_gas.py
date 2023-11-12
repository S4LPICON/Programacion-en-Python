"""
Suponga que las tarifas de una compañía de gas se basan en el consumo de acuerdo con la siguiente información: 

Los primeros 70 metros cúbicos de gas consumidos tiene un costo de 2000 pesos y esto se constituye en tarifa básica (si consume menos de 70 metros cúbicos igual se cobrará los 2000 pesos), 
Para los consumos entre 70 y 200 (incluido) metros cúbicos se cobra a 50 pesos el metro cúbico extra (que sobre pasa 70) más la tarifa básica
Y para consumos por encima de 200 metros cúbicos de gas consumidos se cobrará a 80 pesos por metro cúbico extra (que sobre pasa 200) mas el costo de los primeros 200 metros según condiciones anteriores.
Dada la lectura del contador al inicio de mes y al final del mes (dos números enteros el primero menor que el segundo), en metros cúbicos, calcule el valor de la factura.

Ejemplo calcular_valor_consumo( 1150, 1180) retorna 2000
"""
def calcular_valor_consumo(a,b):
    m_c_g = b -a
    if m_c_g < 70:
        rta = 2000
    else:
        if m_c_g < 200:
            rta = (m_c_g - 70) * 50 +2000
        else:
            rta = (m_c_g - 200) * 80 + (m_c_g - 70) * 50 -500
    return rta
    
    
    """
    si funciona no se toca
    """