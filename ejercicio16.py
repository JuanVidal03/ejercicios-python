"""
Hacer un programa que cree una tabla bidimensional de longitud 5x15 y la cargue con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
"""
# Definir las dimensiones de la tabla
filas = 5
columnas = 15

# Crear una lista vacía para contener la tabla bidimensional
tabla = []

# Crear la tabla bidimensional y asignar los valores
for i in range(filas):
    fila = []
    for j in range(columnas):
        # Verificar si estamos en los límites de la tabla
        if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
            fila.append(1)  # Asignar 1 a los límites
        else:
            fila.append(0)  # Asignar 0 al resto de los elementos
    tabla.append(fila)

# Imprimir la tabla
for fila in tabla:
    print(fila)