"""
Hacer un programa que lea un número entero y como resultado informar si el número es primo o no.
"""
# libreria para limpiar terminal
import os

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Obtener el número del usuario
numero_ingresado = int(input("Ingresa un número entero: "))

# Verificar si es primo e imprimir el resultado
if es_primo(numero_ingresado):
    os.system("clear")
    print(f"{numero_ingresado} es un número primo.")
else:
    os.system("clear")
    print(f"{numero_ingresado} no es un número primo.")