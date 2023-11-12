"""
Calcular la altura de un cono conociendo el volumen y el radio de su base. V=(1/3)Π r2*a , tomando un valor de pi=3.14159265358979323846

ejemplos:

       altura_cono(10, 3.5) retorna 0.3897672075719886
"""
def altura_cono(volumen, radio):
    pi = 3.14159265358979323846
    altura = (3 * volumen) / (pi * (radio**2))
    return altura