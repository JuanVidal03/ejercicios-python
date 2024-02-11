"""
Hacer un programa que implemente una función recursiva para obtener el factorial de un número.
"""
# input del usuario para hacer el factorial
num_usuario = int(input("Ingresa numero al que se le va a hacer el factorial: "))
# inicio de la funcion
def factorial(num):
    # para ser factorial debe ser mayor a 1
    if num == 0:
        return 1
    # factorial de n es n * factorial(n-1)
    else:
        return num * factorial(num - 1)


# imprimir el resultado y llamar a la funcion
print(f"El factorial de {num_usuario} es {factorial(num_usuario)}") 