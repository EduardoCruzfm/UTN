from os import system 
from data_stark import lista_personajes


def mostrar_menu():
    menu = ["\n1.Mostrar nombre de superhéroe", "2.Mostrar nombre y altura de superhéroe", "3.Mostrar superhéroe más alto y el mas bajo", 
        "4.Mostrar promedio de la altura", "5.Mostrar superhéroe más y menos pesado","6.Salir\n"]

    for opcion in menu:
        print(opcion)

def mostrar_lista_nombre():
    #B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for i in range(len(lista_personajes)):
        print(f"{i+1} - Nombre: {lista_personajes[i]['nombre']}")

def mostrar_lista_nombre_altura():
    #C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    for i in range(len(lista_personajes)):
        print(f"{i+1} - Nombre: {lista_personajes[i]['nombre']} - Altura: {lista_personajes[i]['altura']}")

def mostrar_lista_superhéroe_alto_bajo():
    #D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    superheroe_mas_alto = 0
    superheroe_mas_alto_nombre = ""
    ban_mas_alto = True

    for i in range(len(lista_personajes)):

        if ban_mas_alto == True or float(lista_personajes[i]["altura"]) > superheroe_mas_alto:
            superheroe_mas_alto = float(lista_personajes[i]["altura"])
            superheroe_mas_alto_nombre = lista_personajes[i]["nombre"]
            ban_mas_alto = False

    print(f"(+) _ El superheroe mas alto: {superheroe_mas_alto_nombre} - {superheroe_mas_alto} ")
        
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    superheroe_mas_bajo = 0
    superheroe_mas_bajo_nombre = ""
    ban_mas_bajo = True

    for i in range(len(lista_personajes)):

        if ban_mas_bajo == True or float(lista_personajes[i]["altura"]) < superheroe_mas_bajo:
            superheroe_mas_bajo = float(lista_personajes[i]["altura"])
            superheroe_mas_bajo_nombre = lista_personajes[i]["nombre"]
            ban_mas_bajo = False

    print(f"(-) _ El superheroe mas bajo: {superheroe_mas_bajo_nombre} - {superheroe_mas_bajo} ")

def calcular_promedio():
    # F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
    acu_altura = 0
    contador = 0

    for i in range(len(lista_personajes)):
        contador += 1
        acu_altura = acu_altura + float(lista_personajes[i]["altura"]) 

    promedio_altura = acu_altura / contador
    print(f"La altura promedio es : {promedio_altura}")

def calcular_pesos():
    ban_peso = True
    superheroe_mas_pesado = 0
    superheroe_mas_pesado_nombre = ""
    superheroe_mas_liviado = 0
    superheroe_mas_liviado_nombre = ""

    for i in range(len(lista_personajes)):
        #G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
        if ban_peso == True:
            superheroe_mas_pesado_nombre = lista_personajes[i]["nombre"]
            superheroe_mas_pesado = float(lista_personajes[i]["peso"])
            superheroe_mas_liviado_nombre = lista_personajes[i]["nombre"]
            superheroe_mas_liviado = float(lista_personajes[i]["peso"])
            ban_peso = False

        elif float(lista_personajes[i]["peso"]) >  superheroe_mas_pesado :
            superheroe_mas_pesado_nombre = lista_personajes[i]["nombre"]
            superheroe_mas_pesado = float(lista_personajes[i]["peso"])

        elif float(lista_personajes[i]["peso"]) < superheroe_mas_liviado:
            superheroe_mas_liviado_nombre = lista_personajes[i]["nombre"]
            superheroe_mas_liviado = float(lista_personajes[i]["peso"])

    print(f"El superheroe mas pesado es: {superheroe_mas_pesado_nombre} - {superheroe_mas_pesado}")
    print(f"EL superheroe mas liviano es: {superheroe_mas_liviado_nombre} - {superheroe_mas_liviado}")
