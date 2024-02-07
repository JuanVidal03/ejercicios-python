"""
Hacer un programa en Python que almacene la edad de 5 personas. Al final mostrar por pantalla la menor y mayor edad registrada.
"""

def retonar_edad_mayor_menor():
    # aqui se van a almacenar las edades
    edades = []
    # aqui se van a alamacenar la edad mayor y edad menor
    edad_mayor = 0
    edad_menor = float("inf")
    # mostrar el input 5 veces
    for i in range(1, 5+1):
        edad = int(input("Ingresa tu edad: "))
        # agregar edad al array
        edades.append(edad)
    
    # edad menor
    for edad in edades:
        if (edad_menor > edad):
            edad_menor = edad
    # edad mayor
    for edad in edades:
        if(edad_mayor < edad):
            edad_mayor = edad
    
    # imprimiendo los resultados
    print(f"La edad menor registrada es: {edad_menor}")
    print(f"La edad mayor registrada es: {edad_mayor}")
    

retonar_edad_mayor_menor()