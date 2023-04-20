'''
Eduardo Cruz DIV B

2- Listas
La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.


'''

from os import system
system("cls")
palabra_espaniol = ""
palabra_traducida = ""
diccinario = []
error = ""

respuesta = "si"

while respuesta == "si":
    
    palabra_espaniol = input("Ingrese palabra en Español: ")

    for i in range(len(diccinario)):
        if diccinario[i]["Español"] == palabra_espaniol:
            error = diccinario[i]["Español"]

    while palabra_espaniol == error:
        palabra_espaniol = input("ERROR: La palabra ya existe ingrese otra: ")

    palabra_traducida = input("Ingrese palabra traducida en Ingles: ")

    traducciones = {}
    traducciones["Español"] = palabra_espaniol
    traducciones["Ingles"] = palabra_traducida
    diccinario.append(traducciones)

    respuesta = input("Quiere seguir ingresando? ")
    #FIN WHILE

for traduccion in diccinario:
    print(f"""\n{diccinario.index(traduccion)} {traduccion} """)