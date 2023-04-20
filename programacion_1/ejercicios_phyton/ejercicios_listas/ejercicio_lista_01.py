'''
Eduardo Cruz DIV B
//
**
++

1- Listas
Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.


'''
#EJERCICIO SIN LISTA
from os import system
system("cls")

# marca = ""
# año  = 0
# modelo = ""
# precio = 0
# contador = 0
# respuesta = "si"

# while respuesta == "si":
#     contador += 1
#     marca = input("Ingese marca del auto: ")
#     año = int(input("Ingrese año del auto: "))
#     while año < 1970:
#         año = int(input("Reingrese año del auto: "))
#     modelo = input("Ingrese modelo del auto: ")
#     precio = float(input("Ingrese preco: "))
#     while precio < 900000:
#         precio = float(input("Reinngrese preco: "))
    
#     print(f"""Unidad - {contador}
#                 Marca : {marca}
#                 Año : {año}
#                 Modelo :{modelo}
#                 Precio : {precio}
#                     """)

#     respuesta = input("Quiere seguir ingresando? ")
#     #FIN WHILE

####################################################

#EJERCICIO CON LISTA
marca = ""
anio  = 0
modelo = ""
precio = 0
contador = 0
respuesta = "si"

stock_autos = []

while respuesta == "si":
    contador += 1
    marca = input("Ingrese marca del auto: ")
    anio = int(input("Ingrese año del auto: "))
    while anio < 1970:
        anio = int(input("Reingrese año del auto: "))
    modelo = input("Ingrese modelo del auto: ")
    precio = float(input("Ingrese precio: "))
    while precio < 900000:
        precio = float(input("Reinngrese preco: "))

    unidades = {}
    unidades["Marca"] = marca
    unidades["Año"] = anio
    unidades["Modelo"] = modelo
    unidades["Precio"] = precio

    stock_autos.append(unidades)

    respuesta = input("Quiere seguir ingresando? ")
    #FIN WHILE

for stock in stock_autos:
    print(f"""\n{stock}  """)