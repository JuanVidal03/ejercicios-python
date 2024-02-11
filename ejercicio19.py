"""
Hacer un programa que permita guardar la temperatura mínima y máxima para cada uno de los días de una semana (Lunes a Domingo) y al final mostrar en pantalla:
    • La temperatura media de cada día
    • Los días con menos temperatura
    • Leer una temperatura por teclado y mostrar los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
"""
# en esta lista van a estar las temperaturas de los dias
temperaturas = []

# recopilara datos
def temperaturas_dias_de_la_semana():
    # lista con los dias de la semana
    dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    # ingresando los datos de temperatuda de cada dia
    for dia in dias_semana:
        # temperaturas ingresadas por el usuario
        temp_minima = float(input(f"Ingresa la temperatura minima del dia {dia} en grados centigrados: "))
        temp_maxima = float(input(f"Ingresa la temperatura maxima del dia {dia} en grados centigrados: "))
        # calculo de temperatura media
        temp_media = (temp_minima + temp_maxima) / 2
        # agregando cada dato de cada dia a la lista 
        temperaturas.append({"dia": dia, "temperatura_maxima": temp_maxima, "temperatura_minima": temp_minima, "temperatura_media": temp_media})
     
# La temperatura media de cada día
def temperatura_media(arr):
    print("".center(50, "*"))
    print(" La temperatura media de cada dia ".center(50, "*").upper())
    print("".center(50, "*"))
    
    # determinando las temperaturas media
    for dia in arr:
        print(f"El dia {dia["dia"]} la temperatura media fue de: {dia["temperatura_media"]}°C")  

# Los días con menos temperatura
def dias_menor_temp(arr):
    # separara una tarea de otra
    print("".center(50, "*"))
    print(" Dias con menor temperatura ".center(50, "*").upper())
    print("".center(50, "*"))
    
    # aqui se van a guardar los dias con temperatur minima a 10 grados
    dias_con_menor_temperatura = [] 
    # dias con temperatura menores a 10 grados
    for dia in arr:
        if dia["temperatura_minima"] <= float(10):
            dias_con_menor_temperatura.append({"dia": dia["dia"], "temp": dia["temperatura_minima"]})
            
    # verificando si hay alguna temp menor o igual a 10 grados
    if len(dias_con_menor_temperatura) > 0:
        print("Los dias con menor temperatura fueron:")
        for dia in dias_con_menor_temperatura:
            print(f"{dia["dia"]} con una temperatura minima de: {dia["temp"]}°C")
    else:
        print("No hubieron dias con temperaturas menores a 10°C")

# Leer una temperatura por teclado y mostrar los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
def comparar_temp(arr):
    # separara una tarea de otra
    print("".center(50, "*"))
    print(" Input del usuario, comparar temp maximas ".center(50, "*").upper())
    print("".center(50, "*"))
    
    # temperatura del usuario a comparar
    temp_a_comparar = float(input("Ingresa una temperatura para saber si un dia de la semana tuvo esa temperatura maxima: "))
    # donde se van a almacenar los resultados
    temp_maxima = []
    # procedimiento
    for dia in arr:
        if temp_a_comparar == dia["temperatura_maxima"]:
            temp_maxima.append(dia["dia"])
    # verificando si hay alguna temperatura que coincida, y imprimir el resultado
    if len(temp_maxima) > 0:     
        print(f"Los dias que tuvieron temperaturas maximas de {temp_a_comparar}°C, fueron: {", ".join(temp_maxima)}")
            
    else:
        print(f"En ningun dia de la semana la temperatura maxima fue de {temp_a_comparar}°C")


# llamado de las funciones funcion 
temperaturas_dias_de_la_semana()
temperatura_media(temperaturas)
dias_menor_temp(temperaturas)
comparar_temp(temperaturas)