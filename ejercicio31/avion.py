class Avion:
    def __init__(self, numero_vuelo):
        self.numero_vuelo = numero_vuelo
        self.fecha = None
        self.ciudad_origen = None
        self.ciudad_destino = None
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def __str__(self):
        return f"Vuelo {self.numero_vuelo}, fecha {self.fecha}, " \
               f"origen {self.ciudad_origen} - destino {self.ciudad_destino} " \
               f"con {len(self.pasajeros)} pasajeros."