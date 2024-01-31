'''
La nueva reforma tributaria en Colombia propone recaudar un impuesto a los salarios de todos
los colombianos de acuerdo a la siguiente tabla:
Salario Tasa de Impuesto
Entre 12 Millon y 15 millones 3%
Entre 15 Millones y 20 Millones 5%
Entre 20 millones y 30 millones 8%
Más de 30 millones 10%
Escribir un programa en Python que pregunte su salario mensual y muestre por pantalla el
impuesto que debe pagar.
'''

sueldo_usuario = int(input('Ingresa tu sueldo: ')) # pidiendo el valor al usuario
tasa_impuesto = 0 # inicializando el valor de la tasa de impuesto
valor_impuesto_a_pagar = 0 # valor inicial del del total del impuesto
tiene_tasa = False # saber si el aplica la tasa de impuesto

# comparando si el sueldo del usuario está entre 12 y 15 millones
if((sueldo_usuario >= 12000000) and (sueldo_usuario <= 14999999)):
    tasa_impuesto = .03 # valor tasa deimpuesto 
    valor_impuesto_a_pagar = sueldo_usuario * tasa_impuesto # valor total del impuesto
    tiene_tasa = True
    # sueldo entre 15 y 20 millones
elif((sueldo_usuario >= 15000000) and (sueldo_usuario <= 19999999)):
    tasa_impuesto = .05 # valor tasa deimpuesto 
    valor_impuesto_a_pagar = sueldo_usuario * tasa_impuesto # valor total del impuesto
    tiene_tasa = True
    # sueldo entre 20 y 30 millones
elif((sueldo_usuario >= 20000000) and (sueldo_usuario <= 29999999)):
    tasa_impuesto = .08 # valor tasa deimpuesto 
    valor_impuesto_a_pagar = sueldo_usuario * tasa_impuesto # valor total del impuesto
    tiene_tasa = True
    # sueldo mayor de 30 millones
elif(sueldo_usuario >= 30000000):
    tasa_impuesto = .10 # valor tasa deimpuesto 
    valor_impuesto_a_pagar = sueldo_usuario * tasa_impuesto # valor total del impuesto
    tiene_tasa = True
else:
    print("El valor no tiene ninguna tasa de impuesto")


if(tiene_tasa == True):
    # sueldo del usuario menos el impuesto
    sueldo_menos_impuesto = sueldo_usuario - valor_impuesto_a_pagar
    print(f"El valor total del impuesto es: ${int(valor_impuesto_a_pagar)} COP") # imprimiendo el valor total del impuesto
    print(f"El salario del usuario menos el valor del impuesto es: ${int(sueldo_menos_impuesto)} COP") # imprimiendo sueldo del usuario menos el impuesto