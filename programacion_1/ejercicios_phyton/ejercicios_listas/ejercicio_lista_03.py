'''
Eduardo Cruz DIV B

3-
Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.


'''

from os import system
system("cls")

from collections import Counter

numero_ingresado = 0
lista_de_numeros = []
contador = 0
respuesta = "si"

while respuesta == "si":
    
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_de_numeros.append(numero_ingresado)

    respuesta = input("Quiere seguir ingresando? ")
    #FIN WHILE

for i in lista_de_numeros:
    contador += 1
    repetido =  max(lista_de_numeros, key=lista_de_numeros.count)
    print(f" Posicion {lista_de_numeros.index(i)} - {i} {id(i)}")

print(f"El numero mas repetido es :{repetido} ")
