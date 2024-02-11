"""
Para el siguiente triangulo rectángulo solicitar el tamaño de la base que en el ejemplo es de 5.
*
* *
* * *
* * * *
* * * * *
"""
# input para la altura
altura_triangulo = int(input("Ingrese la altura del triangulo: "))

def triangulo_tectangulo(base):
    for i in range(1, base + 1):
        print("*" * i)

# llamado de la funcion
triangulo_tectangulo(altura_triangulo)
