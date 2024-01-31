'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el
cliente es menor de 5 años puede entrar gratis, si tiene entre 5 y 18 años debe pagar 5 mil pesos
y si es mayor de 18 años debe pagar 10 mil pesos.
'''

edad_cliente = int(input('Ingresa tu edad: ')) # edad del cliente
# edad menor a 4
if(edad_cliente < 5):
    print('¡Entras gratis!')
    # edad entre 5 y 17
if(edad_cliente >= 5 and edad_cliente < 18):
    print('Debes pagar $5.000 COP por la entrada')
    # edad mayor a 18
elif(edad_cliente >= 18):
    print('Debes pagar $10.000 COP por la entrada')