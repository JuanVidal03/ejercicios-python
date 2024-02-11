"""
Se debe pedir un número el cuál representa el número de niveles. En el ejemplo el número es 4.
   *
  ***
 *****
*******
"""
# recibe por parametro el numero de asteristicos
def asteriscos(altura):

    asteriscos = 1
    columnas = altura * 2 - 1
    for fila in range(1, altura + 1):
        espacios = (columnas - asteriscos)
        print(espacios * " " + asteriscos * "*" + espacios * " ")
        asteriscos += 2

asteriscos(5)
