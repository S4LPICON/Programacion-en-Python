"""
La nota final de un estudiante de Programación, se compone de los siguientes porcentajes: 60% Examen, 25% Quices y 15% Trabajos. Las calificaciones corresponden a números decimales entre 0 y 5.

Hacer una función que conociendo las tres calificaciones retorne la definitiva

Hacer otra función que conociendo las notas de Quices y trabajos retorne la nota que debe sacar en el examen para aprobar la materia con la nota mínima de 3.0.
ejemplos:

            definitiva(5.0 , 4.5, 2.3) retorna
            debe_obtener_examen(4.5, 2.7)  retorna
"""

def definitiva(examen,quiz,trabajos):
    rta = (examen * 0.60) + (quiz * 0.25) + (trabajos * 0.15)
    return rta
def debe_obtener_examen(quiz,trabajos):
    xd = (quiz * 0.25) + (trabajos * 0.15)
    nma = 3.0
    rta = (nma - (quiz * 0.25) - (trabajos * 0.15)) / 0.6
    return rta