"""
Se debe pedir un número el cuál representa el número de niveles. En el ejemplo el número es 4.
   *
  ***
 *****
*******
"""
# imput para ingresar la altura de la piramide
altura_piramide = int(input("Ingrese la altura que va a tener la piramide: "))

def piramide(altura):
    for i in range(altura):
        print(" " * (altura - i - 1) + "*" * (2 * i + 1))

piramide(altura_piramide)