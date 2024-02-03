"""
Hacer un programa en Python que imprima los números múltiplos de 3 que hay entre dos números
"""
#limpiar terminal
import os
# ingreso de inputs
num_origen = int(input("Ingresa el número desde donde va a iniciar: "))
num_final = int(input("Ingresa el número desde donde va a terminar: "))
# donde se van a almacenar los numeros
resultado_multiplos = []
# va a ir desde el numero iniciaol hasta el final
for index in range(num_origen, num_final+1):
    # si el reciduo es 0 se añade al array
    if(index % 3 == 0):
        resultado_multiplos.append(index)

# imprimiendo el resultado
os.system("clear")
print(f"Los números multiplos de tres entre {num_origen} y {num_final} son: ")
print(resultado_multiplos)