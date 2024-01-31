numeroACombertir = int(input('Ingresa un número: '))
notacionBinaria = []

for i in range(1, numeroACombertir + 1):
    numeroACombertir /= 2 # obteniendo la mitad del numero
    modulo = numeroACombertir
    
    if numeroACombertir >= 1:
        modulo %= 2
        notacionBinaria.append(int(modulo))
    else:
        break
    
notacionBinaria.reverse() # cambiando el sentido del array
notacionBinaria.append(0) # añadiendo un cero al final
notacionBinariaString = " ".join(map(str, notacionBinaria)) # convertiendo el array en un string
print(notacionBinariaString) # imprimiendo el resultado