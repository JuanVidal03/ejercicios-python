"""
Hacer un programa que guarde los nombres y la edades de los aprendices de un curso. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se debe mostrar los siguientes datos:

    • Todos lo alumnos mayores de edad.
    • Los alumnos mayores (los que tienen más edad)
"""
# limpiar terminal
import os

# recolecion de datos
def recoleccion_de_datos():    
    # inicializar inputs usuario
    nombre = None
    edad = None
    # aqui se van a almacenar los nombres y edades cmo diccionarios
    aprendices = []
    # hasta que el nombre sea * se va a repetir el ciclo
    while nombre != "*":
        # input usuario
        nombre = input("Ingresa tu nombre: ").capitalize()
        # para que no se agregue el ultimo dato
        if nombre != "*":
            edad = int(input("Ingresa tu edad: "))
            # agregar la persona al array
            aprendices.append({"nombre": nombre, "edad": edad})
    
    # limpiando la terminal
    os.system("clear")
    # retornando la lista con los aprendices
    return aprendices

# estudiantes mayores de edad
def mayores_de_edad(lista):
    # aqui se van a almacenar los aprendices mayores de edad
    mayores_de_edad = []
    # el mayor del grupo
    mayor_del_grupo = max(lista, key=lambda aprendiz: aprendiz["edad"])
    
    # iterando los aprendices
    for aprendiz in lista:
        # agregando a los estudiantes mayores de edad
        if aprendiz["edad"] >= 18:
            mayores_de_edad.append(aprendiz)
    
    # imprimiendo resultados
    print(f"El aprendiz con mas edad es {mayor_del_grupo["nombre"]} con {mayor_del_grupo["edad"]} años")
    print(f"Los aprendices mayores de edad son: {mayores_de_edad}")
    
    
# funcion que recibe como parametro una lista con los aprendices y retorna el aprendiz mayor y los mayores de edad
mayores_de_edad(recoleccion_de_datos()) 