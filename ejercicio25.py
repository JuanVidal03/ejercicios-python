"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.
"""
# imputs usuario
valor_factura = float(input("Ingresa el valor de la factura: "))
iva_a_aplicar = float(input("Ingrese el porcentaje de IVA a aplicar: "))

# inicio funcion
def calcular_iva(factura, iva=19):
    # valor del iva segun la factura
    valor_del_iva = (factura * iva) / 100
    # valor de la factura total
    factura_total = factura + valor_del_iva
    
    # imprimiendo resultados
    print(f"El total de la factura con el IVA de: ${int(factura_total)} COP, el valor del IVA fue de:${int(valor_del_iva)} COP")
    
calcular_iva(valor_factura, iva_a_aplicar)