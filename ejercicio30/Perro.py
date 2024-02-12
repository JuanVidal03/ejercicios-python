class Perro():
    # constructor
    def __init__(self, nombre:str, peso:float):
        self.nombre = nombre
        self.peso = peso
    
    # metodo inicial
    def __str__(self) -> str:
        return f"nombre: {self.nombre} - pero Kg: {self.peso}"
    
    # metodo mostrar info
    def show_info(self) -> str:
        return f"Nombre: {self.nombre} - Peso Kg: {self.peso}"
    
    # cambiar nombre
    def set_nombre(self, nombre:str):
        self.nombre = nombre
    
    # cambiar peso
    def set_peso(self, peso:float):
        self.peso = peso
    
    # metodo ladrar
    def ladrar(self) -> str:
        return "Landrando..."
    
    # metodo respirar
    def respirar(self) -> str:
        return "Respirando..."