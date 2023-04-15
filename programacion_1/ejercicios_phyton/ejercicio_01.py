'''
Eduardo Cruz
Ejercicio 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo ("barbijo","jabon" o "alcohol")
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
'''
from os import system
system("cls")

# precio_producto = 0
# cantidad_unidades = 0

# tipo_producto = input("Ingrese tipo de producto: ")

# while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
#     tipo_producto = input("ERROR: Reingrese tipo de producto: ")

# precio_producto = float(input("Ingrese precio del producto: "))
# while precio_producto < 1:
#     precio_producto = float(input("ERROR: Reingrese precio del producto: "))

# cantidad_unidades = int(input("Ingrese cantidad de unidades: "))
# while cantidad_unidades < 1:
#     cantidad_unidades = int(input("ERROR: Reingrese cantidad de unidades: "))

# marca_producto = input("Ingrese marca del producto: ")
# fabricante_producto = input("Ingrese fabricante del producto: ")

# print("El tipo de producto es: ", tipo_producto)
# print("El precio del producto es: ", precio_producto)
# print("La cantidad de unidades es: ", cantidad_unidades)
# print("La marca es : ", marca_producto)
# print("El fabricante es :", fabricante_producto)

#############################

def comprar():
    tipo_producto = input("ingrese tipo: ")
    tipo_producto = tipo_producto.lower() #pasar a minuscula

    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        tipo_producto = input("errro reingrese tipo: ")

    precio_producto = float(input("Ingrese precio del producto: "))

    while precio_producto < 0:
        precio_producto = float(input("ERROR: Reingrese precio del producto: "))

    cantidad_unidades = int(input("Ingrese cantidad de unidades: "))
    # while cantidad_unidades.isdigit() < 1:
    while cantidad_unidades < 1:
        cantidad_unidades = int(input("ERROR: Reingrese cantidad de unidades: "))

    marca_producto = input("Ingrese marca del producto: ")
    while not marca_producto.isalpha() : #sino ingresa al go da falso
        print("Marca incorrecto")
        marca_producto = input("ERROR: Reingrese marca del producto: ")


    fabricante_producto = input("Ingrese fabricante del producto: ")
    while not fabricante_producto.isalpha() :
        print("Fabricante incorrecto")
        fabricante_producto = input("ERROR; Reingrese fabricante del producto: ")

    print("El tipo de producto es: ", tipo_producto)
    print("El precio del producto es: ", precio_producto)
    print("La cantidad de unidades es: ", cantidad_unidades)
    print("La marca es : ", marca_producto)
    print("El fabricante es :", fabricante_producto)

comprar()