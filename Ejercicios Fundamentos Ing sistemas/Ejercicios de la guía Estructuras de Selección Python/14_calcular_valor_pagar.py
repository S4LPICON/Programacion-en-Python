"""
Una lavandería ofrece sus servicios a la ciudad de Pamplona de acuerdo a la siguiente tabla que representa el precio del servicio por kilogramo de ropa a lavar.

me dio weba copear lo de la imagen xd




Hacer una función para determinar cuánto debe pagar un cliente por un servicio

calcular_valor_pagar(5,"normal") o calcular_valor_pagar(2,"especial") 
"""
def calcular_valor_pagar(a, b):
    if b == "normal":
        if a <= 2:
            rta = 500 * a
        else:
            rta = 300 * a
    else:
        if a <= 2:
            rta = 450 * a
        else:
            rta = 250 * a
    return rta