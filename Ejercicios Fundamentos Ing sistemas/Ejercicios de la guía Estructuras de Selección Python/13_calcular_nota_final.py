"""
El profesor de programación, acordó con sus estudiantes las siguientes reglas para la calificación final de la materia:

La calificación final se obtiene de 3 notas parciales, que tienen igual peso

Si la definitiva es mayor de 3.5 se le suman 0.4. Es decir, si la nota obtenida es de 3.7 el profesor suma 0.4, luego su nota final será de 4.1 (si la nota calculada da más de 5 la definitiva se deja en 5).

Si la definitiva es menor de 2.5 se le resta 0.3.  Es decir que si la nota obtenida es de 2.2 el profesor resta 0.3, luego su nota final será de 1.9. Si la nota resultante fuese menor que 0 (cero) la definitiva se deja en 0 (cero).

Haga una función que, dadas las 3 notas para un estudiante, calcule la nota final.

calcular_nota_final(3.5 , 2.9 , 4.0)
"""
def calcular_nota_final(nota1, nota2, nota3):
    definitiva = (nota1 + nota2 + nota3) / 3

    if definitiva > 3.5:
        definitiva += 0.4
    elif definitiva < 2.5:
        definitiva -= 0.3
        
    if definitiva > 5:
        definitiva = 5
    elif definitiva < 0:
        definitiva = 0

    return definitiva