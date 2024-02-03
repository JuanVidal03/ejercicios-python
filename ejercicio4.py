'''
La pizzería Napolitana de la Ciudad de Neiva ofrece pizzas vegetarianas y no vegetarianas a
sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación:

    • Ingredientes vegetarianos: Pimiento y tofu.
    • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
ingredientes que lleva
'''
# importar libreria que limpia la terminal
import os

# input usuario
pizza_usuario = input('Ingresa V para pizza vegetariana o NV para una NO vegetariana: ').upper()
# menu base
pizza_base = ['Mozzarella', 'Tomate']

# ingredientes
ingredientes_vegetarianos = ['Pimiento', 'Tofu']
ingredientes_no_vegetarianos = ['Peperoni', 'Jamón', 'Salmón']

# pizza final
pizza_final = []
# ingrediente a añadir
nuevo_ingrediente = None

# funcion que recibe por parametro el array de ingredientes, ya sea vegetariano o no vegetariano
def retornar_menu(arr):
    # limpiando la terminal
    os.system('clear')
    
    # instrucciones iniciales
    print('Los ingredientes que puedes elegir son:')
    print('Debes elegir el número del ingrediente que deseas añadir')
    
    # mostrando las opciones del menú y su opcion a elegir
    for index, ingrediente in enumerate(arr):
        print(f"{index+1}. {ingrediente}")
        
    # nuevo ingrediente añadido
    nuevo_ingrediente = int(input('Ingresa el número correspondiente al ingrediente que deseas: '))
    # copiando el array con los ingredientes base, para añadir el nuevo ingrediente
    pizza_final = pizza_base[:]
    
    # añadiendo el ingrediente seleccionado a la pizza final
    for index, opcion in enumerate(arr):
        new_index = index+1
        if(nuevo_ingrediente == new_index):
            pizza_final.append(opcion)
            os.system("clear")
            print("Ingrediente añadido!");
        else:
            print('Escoge una opcion disponible!')
            
    # retornando la pizza final dependiendo del tipo que sea
    if(pizza_usuario == 'V'):
        print(f"Tu pizza vegetaria quedaria: {", ".join(pizza_final)}")
    else:
        print(f"Tu pizza no vegetaria quedaria: {", ".join(pizza_final)}")
        

# en caso de haber elegido pizza vegetariana
if(pizza_usuario == 'V'):
    retornar_menu(ingredientes_vegetarianos) 
    
# en caso de haber elegido pizza no vegetariana
elif(pizza_usuario == 'NV'):
    retornar_menu(ingredientes_no_vegetarianos)
    
# en caso de ingresar una opcion no disponible
else:
    print('Debes escoger una opción disponible!')