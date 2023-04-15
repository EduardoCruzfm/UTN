'''
Eduardo Cruz DIV B
Ejercicio 04
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
'''
def mostrar():
    peso = 0
    precio_por_kilo = 0
    tipo_variedad = ""
    acu_total = 0
    acu_peso_total = 0
    descuento = 0
    importe_con_descuento = 0
    ban_tipo_mas_caro = True
    tipo_mas_caro_nombre = ""
    tipo_mas_caro_precio = 0

    for x in range(15):

        peso = float(input("Ingrese el peso entre (10 - 100 kls): "))
        while peso < 10 or peso > 100:
            peso = float(input("ERRO Reingrese el peso entre (10 - 100 kls): "))

        precio_por_kilo = float(input("Ingrese el precio: "))
        while precio_por_kilo < 0:
            precio_por_kilo = float(input("Error Reingrese el precio: "))

        tipo_variedad = input("Ingese tipo (vegetal, animal, mezcla): ")
        while tipo_variedad != "vegetal" and tipo_variedad != "animal" and tipo_variedad != "mezcla":
             tipo_variedad = input("ERROR Reingese tipo (vegetal, animal, mezcla): ")

        # A. El importe total a pagar, BRUTO sin descuento.
        acu_total = acu_total + (precio_por_kilo * peso)

        # C. Informar el tipo de alimento más caro.
        if ban_tipo_mas_caro == True or precio_por_kilo > tipo_mas_caro_precio:
            tipo_mas_caro_nombre = tipo_variedad
            tipo_mas_caro_precio = precio_por_kilo
            ban_tipo_mas_caro = False

        # B. El importe total a pagar con descuento (Solo si corresponde).
        acu_peso_total = acu_peso_total + peso

    #FIN DE FOR

    # B. El importe total a pagar con descuento (Solo si corresponde).
    if acu_peso_total > 100:
        descuento = -15
    elif acu_peso_total > 300:
        descuento = -25
    else:
        descuento = 0
    # precioFinal = TOTAL + (TOTAL * descuento / 100);

    importe_con_descuento = acu_total + (acu_total * descuento / 100)

    # C. Informar el tipo de alimento más caro.
    
    print(f"El importe total a pagar, BRUTO sin descuento es: {acu_total}")
    print(f"El importe total a pagar con descuento es: {importe_con_descuento}")
    print(f"El tipo de alimento más car es: {tipo_mas_caro_nombre} con: {tipo_mas_caro_precio}")

mostrar()