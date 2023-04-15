'''
Eduardo Cruz
DIV B
Desafío #00:

A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener
'''

from data_stark import lista_personajes
from os import system
system("cls")

# #B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# for i in range(len(lista_personajes)):

#     print(f"{i+1} - Nombre: {lista_personajes[i]['nombre']}")

# #C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# # la altura del mismo
# for i in range(len(lista_personajes)):

#     print(f"{i+1} - Nombre: {lista_personajes[i]['nombre']} - Altura: {lista_personajes[i]['altura']}")


#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
superheroe_mas_alto = 0
superheroe_mas_alto_nombre = ""
ban_mas_alto = True

for i in range(len(lista_personajes)):

    if ban_mas_alto == True or float(lista_personajes[i]["altura"]) > superheroe_mas_alto:
        superheroe_mas_alto = float(lista_personajes[i]["altura"])
        superheroe_mas_alto_nombre = lista_personajes[i]["nombre"]
        ban_mas_alto = False

print(f"El superheroe mas alto: {superheroe_mas_alto_nombre} - {superheroe_mas_alto} ")
    