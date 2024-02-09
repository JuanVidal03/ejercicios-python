"""
Hacer un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos)
"""
# input del usuario
palabra_usuario = None
# palabras agregadas por el usuario, aqui van a estar todas las palabras, incluso las repetidas
palabras = []
# va a repetir el ciclo hasta que el usuario agregue uno
while palabra_usuario != "1":
    # input donde el usuario va a ingresar la palabra
    print("Ingresa una palabra, si ingresas '1' el programa acabara")
    palabra_usuario = input("Ingresa una palabra: ")
    
    if palabra_usuario != '1':
        # agregar palabra al array
        palabras.append(palabra_usuario)

# eliminamos las palabras repetidas
set_palabras_sin_repetir = set(palabras)
# convertimos los elementos a una lista
palabras_sin_repetir = list(set_palabras_sin_repetir)
# imprimimos un array sin elementos repetidos
print(palabras_sin_repetir)