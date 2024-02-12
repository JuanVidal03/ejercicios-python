# importar clases
from Perro import Perro
from Gato import Gato
from Pez import Pez

# instanciar objetos
perro = Perro("Firulais", 23.70)
print(perro.ladrar())
print(perro.show_info())

gato = Gato("Michi", 15.50)
print(gato.maullar())
print(gato.show_info())

pez = Pez("Nemo", 5.50)
print(pez.nadar())
print(pez.show_info())