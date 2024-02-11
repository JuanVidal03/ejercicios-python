"""
Hacer un programa que mediante el uso de funciones calcule el área de figuras geometricas como círculo, triángulo, cuadrado.
"""
# libreria para hacer operaciones matematicas
import math
import os

# area circulo
def area_circulo(radio):
    return math.pi * radio ** 2

# area triangulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# area cuadrado
def area_cuadrado(lado):
    return lado ** 2

# Función principal para solicitar al usuario la figura y sus dimensiones
def app():
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Cuadrado")

    opcion = int(input("Seleccione la figura para calcular su área (1/2/3): "))

    #limpiar terminal
    os.system("clear")
    match opcion:
        case 1:
            radio = float(input("Ingrese el radio del círculo: "))
            print("El área del círculo es:", area_circulo(radio))
        case 2:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print("El área del triángulo es:", area_triangulo(base, altura))
        case 3:
            lado = float(input("Ingrese el lado del cuadrado: "))
            print("El área del cuadrado es:", area_cuadrado(lado))
        case _:
            print("Debes ingresar una opcion valida")

# llamar a la funcion principal
app()
