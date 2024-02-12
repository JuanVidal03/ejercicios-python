"""
Hacer un programa en Python que implemente una función que reciba como parámetros un año y un mes, y la función debe devolver el número de días del mes dado del año especifico.
"""

def obtener_dias_en_mes(anio, mes):
    meses_de_30_dias = {4, 6, 9, 11}  # Meses con 30 días
    meses_de_31_dias = {1, 3, 5, 7, 8, 10, 12}  # Meses con 31 días

    # Validar que el mes esté en el rango válido (1-12)
    if mes < 1 or mes > 12:
        return "Error: Mes no válido"

    # Determinar el número de días en el mes
    if mes == 2:
        # Febrero - verificar si es un año bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29  # Año bisiesto, febrero tiene 29 días
        else:
            return 28  # Año no bisiesto, febrero tiene 28 días
    elif mes in meses_de_30_dias:
        return 30
    elif mes in meses_de_31_dias:
        return 31

anio_ingresado = int(input("Ingrese el año: "))
mes_ingresado = int(input("Ingrese el mes (1-12): "))

resultado = obtener_dias_en_mes(anio_ingresado, mes_ingresado)
if type(resultado) == int:
    print(f"El mes {mes_ingresado} del año {anio_ingresado} tiene {resultado} días.")
else:
    print(resultado)