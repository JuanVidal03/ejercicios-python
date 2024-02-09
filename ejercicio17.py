"""
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
"""
# libreria para tener numeros random
import random
# lista donde se van a almacenar los numeros aleatorios
lista_num_aleatorios = []
# agregando 10 numeros aleatorios a la lista
for i in range(1, 10+1):
    # generando num random
    num_random = random.randint(0, 100)
    # agregar num a la lista
    lista_num_aleatorios.append(num_random)
# ordenando la lista
num_ordenados = sorted(lista_num_aleatorios)
print(f"La lista inicial fue: {lista_num_aleatorios}")
print(f"La lista ordenada es: {num_ordenados}")