"""
Hacer un programa en Python que implemente una función que recibe como parámetro una lista con números enteros y la función debe retornar dos listas ordenadas; una lista con números pares y otra lista con números impares
"""
# lista prueba
lista_numeros = [1, 45, 90, 34, 2, 76, 65, 87]

# inicio de la funcion
def listas(lista):
    # lista ordenada
    lista_ordenada = sorted(lista)
    # almacenar numeros parea e impares
    pares = []
    impares = []
    
    # sacando numeros pares e impares
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    # imprimiendo los resultados
    print(f"La lista ingresada fue: {lista}")
    print(f"La lista ordenada seria: {lista_ordenada}")
    print(f"Los numeros pares son: {pares}")
    print(f"Los numeros impares son: {impares}")

listas(lista_numeros)