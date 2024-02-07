"""
Hacer un programa en Python que simule un menú como el siguiente:
MENÚ DE OPCIONES
1. Opción 1
2. Opción 2
3. Opción 3
4. Salir
Ingrese Opción:
En las opcions 1 a la 3 mostrar un mensaje y retornar al menú. Si selecciona la opción 4 de salir debe terminar el programa.
"""
# libraria para limpiar la terminal
import os
# maneja que el ciclo no se vuelva infinito
controlador = True
# inicio de ciclo, hasta que cotrolador no sea True va a seguir dando vueltas
while(controlador):
    # menu de opciones
    print("MENU DE OPCIONES".center(30, "*"))
    print("1. Opcion 1\n2. Opcion 2\n3. Opcion 3\n4. Salir\nIngresa el numero de la opcion que quieras")
    # opcion digitada por el usuario
    opcion = int(input("Ingresa tu opcion: "))
    
    # limpiando la terminal
    os.system("clear")
    # inicio de las opciones
    match opcion:
        case 1:
            print("Seleccionaste la opcion 1".center(50, "*"))
        case 2:
            print("Seleccionaste la opcion 2".center(50, "*"))
        case 3:
            print("Seleccionaste la opcion 3".center(50, "*"))
        case 4:
            print("Saliste del programa!".center(50, "*"))
            break