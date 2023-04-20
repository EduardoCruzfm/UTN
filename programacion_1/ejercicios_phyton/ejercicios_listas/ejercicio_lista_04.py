'''
Eduardo Cruz DIV B

4-
Debemos desarrollar un algoritmo que permita computar los votos del Senado de
Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
la sesión. Si el senador está presente, se deberá pedir el valor del voto
El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
(validar). El valor por defecto para los senadores ausentes será Abstención.
Se deberá Informar:

o Cantidad total de senadores.
o Cantidad de senadores presentes.
o Cantidad y porcentaje de votos afirmativos.
o Cantidad y porcentaje de votos negativos.
o Cantidad y porcentaje de abstenciones.
o Generar una lista de senadores por cada tipo de voto y mostrarlas por
pantalla.


'''
#EJERCICIO SIN LISTA
from os import system
system("cls")

senadores = ""
votos = ""
presente = ""
contador_total = 0
contador_afirmativos = 0
respuesta = "si"

while respuesta == "si":
    senadores = input("Ingrese nombre de senador: ")

    presente = input("Ingrese si esta presente si/no: ")
    while presente != "si" or presente != "no":
        presente = input("ERROR Reingrese si esta presente si/no: ")
    
    if presente == "si":
        votos = input("Ingese voto 'Afirmativo', 'Negativo'")
        while votos != "Afirmativo" or votos != "Negativo" or votos != "Abstención":
            votos = input("ERROR: Ingese voto 'Afirmativo', 'Negativo' ")
    else: 
        votos = "Abstención"
        
    
    # Cantidad total de senadores.
    contador_total = contador_total + 1

    # Cantidad y porcentaje de votos afirmativos.
    if votos == "Afirmativo":
          contador_afirmativos = contador_afirmativos + 1
    

respuesta = input("Quiere seguir ingresanod votos? si/no")
#FIN WHILE

