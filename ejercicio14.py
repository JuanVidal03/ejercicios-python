"""
Hacer un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista
"""
# libreria para limpiar la terminal
import os
# array donde se van a almacenar las palabras
palabras = []
# se inicializa la variable donde va a estar el input de la palabra
palabra = None
# hasta que el usuario ingrese 1 se va a repetir el blouqe de codigo
while(palabra != "1"):
    os.system("clear")
    # ingresar palabra
    print("Ingresa una palabra por input, si ingresas 1 se saldra del programa")
    palabra = input("Ingresa una palabra: ")
    # si palabra es 1 el ciclo terminara
    if (palabra != "1"):
        # agregar palabra en mayuscula al array en caso de ser distinto a 1
        palabras.append(palabra.upper())

# funcion que cuenta las palabras que esten dentro de un array
def contar_palabras(arr):
    os.system("clear")
    # palabra que el usuario va a buscar
    buscar_palabra = input("Escrina la palabra que quieres buscar: ").upper()
    # variable que llevera el registro de las variables repetidas
    conteo = 0
    # iterar los elementos del array de palabras
    for palabra_arr in arr:
        
        # verificando si la palabra se encuentra dentro del array
        if (buscar_palabra == palabra_arr):
            conteo += 1
        else:
            conteo = 1
    # mostrando por terminal 
    print(f"La palabra {buscar_palabra.capitalize()} se encuentra {conteo} veces en la lista de palabras")

# llamado de la funcion
contar_palabras(palabras)