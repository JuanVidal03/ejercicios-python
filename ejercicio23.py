"""
Hacer un programa en Python que implemente una función que reciba como parámetro una lista con números enteros y como resultado debe devolver la suma de los números.
"""
# lista que se va a sumar
lista_numeros = [11, 24, 23, 46, 98, 87,]

def sumar_num_dentro_de_lista(lista):
    # aqui se van a almacenar la suma de los numeros dentro de la lista
    suma = 0
    # iterando la lista y sumando sus elementos
    for numero in lista:
        suma += numero
    # imprimir resultado
    print(f"La suma de los numeros dentro de la lista es: {suma}")


sumar_num_dentro_de_lista(lista_numeros)