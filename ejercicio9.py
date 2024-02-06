""""
Hacer un programa que lea la edad de 5 personas y para cada una de ellas informar en que fase de vacunación contra el covid es asignado. Ver tabla:
Rango de Edad Fase
>=80 años Fase 1
>=70 y <80 Fase 2
>=60 y <70 Fase 3
>=30 y <60 Fase 4
>=18 y <30 Fase 5
<18 En espera de Autorización
"""
# libreria para limpriar comsola
import os
# aqui se van a almacenar las edades
edades = []
# funcion que recolecta las edades
def recaudar_edades():
    # va a repetir la información 5 veces
    for i in range(1, 5+1):
        # nombre del usuario
        nombre = input("Ingresa el nombre de la persona: ")
        # edad del usuario
        usuario_edad = int(input(f"Ingresa la edad de la persona No.{i}: "))
        # añadir la edad al array y el número de la persona al array, generando tambien un array
        edades.append(
            {
                "id_persona": i,
                "Nombre_persona": nombre,
                "edad": usuario_edad
            }
        )
    
    # limpiando la terminal
    os.system("clear")
    # recorriendo os diccionarios para comparar las edades
    for diccionario in edades:
        # fase 1
        if(diccionario["edad"] >= 80):
            print(f"Nombre: {diccionario["Nombre_persona"]}, Edad: {diccionario["edad"]}, Fase: Fase de vacunacion Fase 1")
            # fase 2
        elif(diccionario["edad"] >= 70 and diccionario["edad"] < 80):
            print(f"Nombre: {diccionario["Nombre_persona"]}, Edad: {diccionario["edad"]}, Fase: Fase de vacunacion Fase 2")
            # fase 3
        elif(diccionario["edad"] >= 60 and diccionario["edad"] < 70):
            print(f"Nombre: {diccionario["Nombre_persona"]}, Edad: {diccionario["edad"]}, Fase: Fase de vacunacion Fase 3")
            # fase 4
        elif(diccionario["edad"] >= 30 and diccionario["edad"] < 60):
            print(f"Nombre: {diccionario["Nombre_persona"]}, Edad: {diccionario["edad"]}, Fase: Fase de vacunacion Fase 4")
            # fase 5
        elif(diccionario["edad"] >= 18 and diccionario["edad"] < 30):
            print(f"Nombre: {diccionario["Nombre_persona"]}, Edad: {diccionario["edad"]}, Fase: Fase de vacunacion Fase 5")
            # En espera de Autorización
        else:
            print(f"Nombre: {diccionario["Nombre_persona"]}, Edad: {diccionario["edad"]}, Fase: En espera de autorizacion.")
            

recaudar_edades()