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

# aqui se van a almacenar las edades
edades = []
# funcion que recolecta las edades
def recaudar_edades():
    # va a repetir la información 5 veces
    for i in range(1, 5+1):
        # input del usuario
        usuario_edad = int(input(f"Ingresa la edad de la persona No.{i}: "))
        # añadir la edad al array
        edades.append(usuario_edad)
    
    print(f"Las edades ingresadas fueron: {", ".join(map(str, edades))}") 
    
    
# funcion que obtiene el numero mayor
def num_mayor(arr):
    # inicializando la comparación
    num_mayor = 0
    # recorriendo el array de edades para saber el numero mayor
    for numero in arr:
        # cambiando el número mayor 
        if(numero > num_mayor):
            num_mayor = numero
    # retorna el número mayor
    return num_mayor

# funcion que obtiene el número menor
def num_menor(arr):
    # obteniendo el número mayor
    num_menor = num_mayor(arr)
    # recorriendo el array de edades para saber el numero menor
    for numero in arr:
        # comparando los numeros del array con el numero mayo
        if(numero < num_menor):
            num_menor = numero
    # retorna el número mayor
    return num_menor


# llamado de las funciones
recaudar_edades()
print(f"El número mayor es: {num_mayor(edades)}")
print(f"El número menor es:{num_menor(edades)}")
