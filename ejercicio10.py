"""
Hacer un programa que calcule el factorial de un número teniendo en cuenta la siguiente formula:
𝑛!=𝑛∗(𝑛−1)!
0!=1
1!=1
Ejemplo : 5! = 5 * 4 * 3 * 2 * 1
"""
# input del usuairo
num_usuario = int(input("Ingresa un numero: "))

def factorial(num):
    # alamacenar numeros factoriales
    numeros_factoriales = []
    # iterandolos y añadiendolos al array
    for i in range(1, num+1, +1):
        numeros_factoriales.append(i)
    # empezar por el primer numero del factorial    
    inicio = numeros_factoriales[0]
    # haciendo las multiplicaciones del factorial
    for i in numeros_factoriales:
        inicio = inicio * i
        i = i+1
    # imprimo el resultado 
    print(f"El factorial de {num} es: {inicio}")
# llamado de la funcion
factorial(num_usuario)