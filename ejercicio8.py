"""
Hacer un programa en Python que imprima las tablas de multiplicar del 5, 6 7 8 y 9
"""
# funcion que recibe por parametro el numero que se va a 
def tabla_multiplicar(num):

    for i in range(1, 10+1):
        result = num * i
        print(f"{num}x{i}={result}")
        
# ingreso del numero del usuario
num_usuario = int(input("Escribe el numero para hacer su tabla de multiplicar: "))
# llamado de la funcion
tabla_multiplicar(num_usuario)