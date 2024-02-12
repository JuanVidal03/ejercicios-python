"""
Hacer un programa en Python que utilizando y listas y otras estructuras de programación permite simular los procesos de un banco relacionado con las cuentas de ahorro. La aplicación debe permitir lo siguiente:

    a. Crear una cuenta de ahorros. Las cuentas de ahorro tienen el siguiente código: año-consecutivo.
        Ejemplo: 2022-1, la siguiente sería 2022-2, 2022-3 y así sucesivamente. El año se tiene que obtener de la fecha actual.
    b. Agregar los datos del cliente dueño de una cuenta de ahorros con los siguientes datos: identificación, nombre completo y correo electrónico.
    c. De las cuentas de ahorro se requieren conocer los siguientes datos: código de la cuenta,
    fecha de creación saldo.
    d. Consignar a una determinada cuenta
    e. Retirar a una determinada cuenta
    
La solución debe presentar un menú de opciones así:

    MENÚ BANCO ADSO 2449133
    1. Crear Cuenta
    2. Consignar Cuenta
    3. Retirar Cuenta
    4. Consultar Cuenta Por Código
    5. Consultar Cuenta por Identificación Cliente
    6. Listar Cuentas
    7. Salir
    Ingrese Opción (1-7): 
"""

# Se importa el módulo datetime, para trabajar con fechas y horas
import datetime

# Se crea la clase cuenta de ahorros.
class CuentaAhorro:
    def __init__(self, codigo, identificacion, nombre, correo):
        self.codigo = codigo
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d")
        self.saldo = 0

# Se crea la clase banco
class Banco:
    def __init__(self):
        self.cuentas = []

    # Se crean los métodos de la clase
    def crear_cuenta(self, identificacion, nombre, correo):
        codigo = self.generar_codigo()
        cuenta = CuentaAhorro(codigo, identificacion, nombre, correo)
        self.cuentas.append(cuenta)
        print("Cuenta creada exitosamente.")
        print(f"Código de cuenta: {codigo}")

    def generar_codigo(self):
        year = datetime.datetime.now().year
        consecutivo = len([cuenta for cuenta in self.cuentas if cuenta.fecha_creacion.startswith(str(year))]) + 1
        return f"{year}-{consecutivo}"

    def consignar(self, codigo, monto):
        for cuenta in self.cuentas:
            if cuenta.codigo == codigo:
                cuenta.saldo += monto
                print("Consignación exitosa.")
                print(f"Nuevo saldo para la cuenta {codigo}: {cuenta.saldo}")
                return
        print("Cuenta no encontrada.")

    def retirar(self, codigo, monto):
        for cuenta in self.cuentas:
            if cuenta.codigo == codigo:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
                    print("Retiro exitoso.")
                    print(f"Nuevo saldo para la cuenta {codigo}: {cuenta.saldo}")
                    return
                else:
                    print("Saldo insuficiente.")
                    return
        print("Cuenta no encontrada.")

    def consultar_por_codigo(self, codigo):
        for cuenta in self.cuentas:
            if cuenta.codigo == codigo:
                print(f"Código de cuenta: {cuenta.codigo}")
                print(f"Fecha de creación: {cuenta.fecha_creacion}")
                print(f"Saldo: {cuenta.saldo}")
                print(f"Identificación del cliente: {cuenta.identificacion}")
                print(f"Nombre del cliente: {cuenta.nombre}")
                print(f"Correo electrónico del cliente: {cuenta.correo}")
                return
        print("Cuenta no encontrada.")

    def consultar_por_identificacion(self, identificacion):
        cuentas_encontradas = [cuenta for cuenta in self.cuentas if cuenta.identificacion == identificacion]
        if cuentas_encontradas:
            for cuenta in cuentas_encontradas:
                print(f"Código de cuenta: {cuenta.codigo}")
                print(f"Fecha de creación: {cuenta.fecha_creacion}")
                print(f"Saldo: {cuenta.saldo}")
                print(f"Identificación del cliente: {cuenta.identificacion}")
                print(f"Nombre del cliente: {cuenta.nombre}")
                print(f"Correo electrónico del cliente: {cuenta.correo}")
        else:
            print("No se encontraron cuentas asociadas a esta identificación.")

    def listar_cuentas(self):
        if self.cuentas:
            for cuenta in self.cuentas:
                print(f"Código de cuenta: {cuenta.codigo}")
                print(f"Fecha de creación: {cuenta.fecha_creacion}")
                print(f"Saldo: {cuenta.saldo}")
                print(f"Identificación del cliente: {cuenta.identificacion}")
                print(f"Nombre del cliente: {cuenta.nombre}")
                print(f"Correo electrónico del cliente: {cuenta.correo}")
        else:
            print("No hay cuentas registradas en el banco.")


# Función para mostrar el menú y manejar las opciones
def mostrar_menu(banco):
    print("MENÚ BANCO ADSO 2669742")
    print("1. Crear Cuenta")
    print("2. Consignar Cuenta")
    print("3. Retirar Cuenta")
    print("4. Consultar Cuenta Por Código")
    print("5. Consultar Cuenta por Identificación Cliente")
    print("6. Listar Cuentas")
    print("7. Salir")

    opcion = input("Ingrese Opción (1-7): ")
    if opcion == '1':
        identificacion = input("Ingrese la identificación del cliente: ")
        nombre = input("Ingrese el nombre completo del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        banco.crear_cuenta(identificacion, nombre, correo)
    elif opcion == '2':
        codigo = input("Ingrese el código de la cuenta: ")
        monto = float(input("Ingrese el monto a consignar: "))
        banco.consignar(codigo, monto)
    elif opcion == '3':
        codigo = input("Ingrese el código de la cuenta: ")
        monto = float(input("Ingrese el monto a retirar: "))
        banco.retirar(codigo, monto)
    elif opcion == '4':
        codigo = input("Ingrese el código de la cuenta: ")
        banco.consultar_por_codigo(codigo)
    elif opcion == '5':
        identificacion = input("Ingrese la identificación del cliente: ")
        banco.consultar_por_identificacion(identificacion)
    elif opcion == '6':
        banco.listar_cuentas()
    elif opcion == '7':
        print("Gracias por utilizar el Banco ADSO 2449133. ¡Hasta luego!")
        return
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

    mostrar_menu(banco)


if __name__ == "__main__":
    banco = Banco()
    mostrar_menu(banco)
