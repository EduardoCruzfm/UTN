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
counter = Counter(lista_de_numeros)

while respuesta == "si":
    
    numero_ingresado = int(input("Ingrese un numero: "))

    lista_de_numeros.append(numero_ingresado)

    respuesta = input("Quiere seguir ingresando? ")
    #FIN WHILE



# for traduccion in diccinario:
#     print(f"""\n{diccinario.index(traduccion)} {traduccion} """)

elementos_ordenados = counter.most_common()
first = elementos_ordenados[0]
second = elementos_ordenados[1]
# // Ignora todos los valores intermedios
last = elementos_ordenados[-1]

for i in lista_de_numeros:
    contador += 1
    # print(f" {lista_de_numeros.index(i)} {lista_de_numeros[0]}")
    print(f" Posicion {lista_de_numeros.index(i)} - {i} {id(i)}")

print(f"{first}-{second}")
