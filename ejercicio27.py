"""
Hacer un programa que implemente una función que verifique si tres lados de ciertas longitudes pueden formar un triángulo. La función recibe tres parámetros, uno para cada lado. Retornará True si todos los lados puedes formar un triángulo y False de lo contrario. Para validar si es un triángulo tenga en cuenta lo siguiente: La suma de dos lados tiene que ser mayor que la longitud del tercer lado. En el mismo programa implementar una función para que verifique si el triángulo es un triángulo rectángulo.

Hacer uso del teorema de Pitágoras:
𝐶2 = 𝑎2 + 𝑏2
"""
# limpiar terminal
import os
# lados del triangulo
lado1 = int(input("Ingrese la medida del 1 lado en cm: "))
lado3 = int(input("Ingrese la medida del 2 lado en cm: "))
lado2 = int(input("Ingrese la medida del 3 lado en cm: "))

# saber si es un triangulo
def si_es_triangulo(lado1, lado2, lado3):
    # limpiar terminal
    os.system("clear")
    
    # saber si es un triangulo o no
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
        print("Es un triangulo".center(50, "*"))
        
        # VERIFICANDO SI ES UN TRIANGULO RECTANGULO
        # ordenando los lados para saber cual es la hipotenusa
        lista_ordenados = sorted([lado1, lado2, lado3])
        
        # formula temorema de pitagoras
        formula_pitagoras = (lista_ordenados[0]**2 + lista_ordenados[1]**2) == lista_ordenados[2]**2
        
        # retorna el mensaje si es un triangulo rectangulo o no
        if formula_pitagoras:
            print(f"Es un triangulo rectangulo con catetos: {lista_ordenados[0]}cm y {lista_ordenados[1]}cm, y con una hipotenusa de {lista_ordenados[2]}cm")
        # en caso de no ser un triangulo rectangulo
        else:
            print(" El triangulo no es rectangulo ".center(50, "*"))
    # en caso de no formar un triangulo
    else:
        print("No es un triangulo".center(50, "*"))
    

# llamado de la funcion
si_es_triangulo(lado1, lado3, lado2)