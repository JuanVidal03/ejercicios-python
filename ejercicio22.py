"""
Hacer un programa en Python que implemente una función que reciba como parámetro una cadena de texto y una palabra. La función debe devolver la cantidad de veces que existe la palabra en todo el texto
"""
# inputs del usuario
oracion = input("Ingresa una oracion: ")
palabra_buscar = input("Ingresa la palabra a buscar en la oracion: ")


def encontrar_palabra_en_oracion(oracion:str, palabra:str):
    # hacer que tanto el texto como la oracion sean iguales
    oracion_minuscula = oracion.lower()
    palabra_minuscula = palabra.lower()
    
    # separa las palabras de la oracion y las convierte en una lista
    palabras_en_la_oracion = oracion_minuscula.split()
    
    # contar la cantidad de veces que esta una misma palabra en la lista de la oracion
    conteo_palabras = palabras_en_la_oracion.count(palabra_minuscula)
    
    print(f"La palabra: '{palabra}', se encuenta {conteo_palabras} veces en la oracion: '{oracion}'")  

# llamado de la funcion
encontrar_palabra_en_oracion(oracion, palabra_buscar)