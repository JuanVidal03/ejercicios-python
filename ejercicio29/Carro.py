class Carro():
    # constructor
    def __init__(self, placa:str, marca:str, modelo:int, color:str):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    # metodo inicial
    def __str__(self) -> str:
        return f"{self.placa} - {self.marca} - {self.modelo} - {self.color}"
    
    # obtener placa
    def get_placa(self) -> str:
        return self.placa
    
    # obtener modelo
    def get_modelo(self) -> int:
        return self.modelo
    
    # actualiza placa
    def set_placa(self, placa:str):
        self.placa = placa
        
    # actualizar modelo
    def set_modelo(self, modelo:int):
        self.modelo = modelo

# creando instancias
carro1 = Carro("ELB95E", "Mazda", "2023", "Azul Artico")
print(carro1.get_modelo()) # obteniendo el modelo
print(carro1.get_placa()) # obteniendo placa

carro1.set_modelo(2022) # cambiando el modelo
carro1.set_placa("ELB97D") # cambiando la placa

print(carro1.get_modelo()) # obteniendo el modelo
print(carro1.get_placa()) # obteniendo placa