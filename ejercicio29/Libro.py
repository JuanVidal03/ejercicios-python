class Libro():
    # constructor
    def __init__(self, titulo:str, autor: str, num_pag:int):
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag
    
    # obteniendo titulo
    def get_titulo(self) -> str:
        return self.titulo
    
    # obteniendo autor
    def get_autor(self) -> str:
        return self.autor
    
    # num de paginas
    def get_num_pag(self) -> int:
        return self.num_pag
    
    # actualizando el titulo
    def set_titulo(self, titulo:str):
        self.titulo = titulo
        
    # actualizar el autor
    def set_autor(self, autor:str):
        self.autor = autor
    
    # actualizar num de paginas
    def set_num_pag(self, num_pag:int):
        self.num_pag = num_pag
        
# creando instancia
libro1 = Libro("El retrato de Dorian Grey", "Oscar Wilde", 254)
print(libro1.get_titulo()) # obteniendo titulo
print(libro1.get_autor()) # obteniendo autor
print(libro1.get_num_pag()) # obteniendo num paginas

libro1.set_titulo("Se ha cambiado el titulo") # cambio de titulo
libro1.set_autor("Se ha cambiado el autor") # cambio autor
libro1.set_num_pag(234) # cambio num paginas

print(libro1.get_titulo()) # obteniendo titulo
print(libro1.get_autor()) # obteniendo autor
print(libro1.get_num_pag()) # obteniendo num paginas