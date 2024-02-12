import avion
import pasajero

def main():
    avion_1 = avion.Avion("XYZ123")
    avion_1.fecha = "2023-05-01"
    avion_1.ciudad_origen = "Bogotá"
    avion_1.ciudad_destino = "Medellín"

    pasajero_1 = pasajero.Pasajero("Juan Pérez", "123456789")
    pasajero_2 = pasajero.Pasajero("Ana María Gómez", "987654321")

    avion_1.agregar_pasajero(pasajero_1)
    avion_1.agregar_pasajero(pasajero_2)

    print(avion_1)

if __name__ == "__main__":
    main()