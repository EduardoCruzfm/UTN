'''
Eduardi Cruz DIV B
Ejercicio 03
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:

A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
'''


def mostrar():
    respuesta = "si"
    acu_edad_femenino = 0
    con_edad_femenino = 0
    con_nacho_julieta = 0
    con_votos_total = 0
    con_votos_nacho = 0
    con_votos_julieta = 0
    con_votos_marcos = 0
    porcentaje_nacho = 0
    porcentaje_julieta = 0
    porcentaje_marcos = 0
    msj_porcentaje_nacho = ""
    msj_porcentaje_julieta = ""
    msj_porcentaje_marcos = ""
    ban_votante_mas_joven = True
    votante_mas_joven_nombre = ""
    votante_mas_joven_edad = 0
    msj_votante_mas_joven = ""
    participante_ganador = ""



    while respuesta == "si":

        nombre_votante = input("Ingrese su nombre:  ")

        edad_votante = int(input("Ingrese su edad:  "))
        while edad_votante < 14:
            edad_votante = int(input("ERROR: Reingrese su edad:  "))

        genero_votante = input("Ingrese genero: masculino, femenino, nobinario  ")
        while genero_votante != "masculino" and genero_votante != "femenino" and genero_votante != "nobinario":
            genero_votante = input("ERROR: Reingrese genero: masculino, femenino, nobinario  ")

        nombre_participante = input("Ingrese nombre del participante: Nacho, Julieta y Marcos ")
        while nombre_participante != "Nacho" and nombre_participante != "Julieta" and nombre_participante != "Marcos":
            nombre_participante = input("ERROR: Reingrese nombre del participante: Nacho, Julieta y Marcos  ")

        respuesta = input("Quiere seguir votando?  ")

        # A. El promedio de edad de las votantes de género femenino
        if genero_votante == "femenino":
            acu_edad_femenino = acu_edad_femenino + edad_votante
            con_edad_femenino += 1

        # B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
        if genero_votante == "masculino":
            if (edad_votante > 24 and edad_votante < 41) and (nombre_participante == "Nacho" or nombre_participante == "Julieta"):
                con_nacho_julieta += 1

        # D. Nombre de cada participante y porcentaje de los votos qué recibió.    
        con_votos_total = con_votos_total + 1

        # match nombre_participante:
        #     case "Nacho":
        #         con_votos_nacho = con_votos_nacho + 1
        #          #  C. Nombre del votante más joven que votó a Nacho.
        #         if ban_votante_mas_joven == True or edad_votante < votante_mas_joven_edad:
        #             votante_mas_joven_nombre = nombre_votante
        #             votante_mas_joven_edad = edad_votante
        #             ban_votante_mas_joven = False
        #     case "Julieta":
        #         con_votos_julieta = con_votos_julieta + 1
        #     case "Marcos": 
        #         con_votos_marcos = con_votos_marcos + 1

        if nombre_participante == "Nacho":
            con_votos_nacho = con_votos_nacho + 1
            # C. Nombre del votante más joven que votó a Nacho.
            if ban_votante_mas_joven == True or edad_votante < votante_mas_joven_edad:
                votante_mas_joven_nombre = nombre_votante
                votante_mas_joven_edad = edad_votante
                ban_votante_mas_joven = False

        elif nombre_participante == "Julieta":
            con_votos_julieta = con_votos_julieta + 1
        else:
            con_votos_marcos = con_votos_marcos + 1
        
        #FIN WHILE

    # A. PROMEDIO FEMENINO
    if con_edad_femenino > 0:
        promedio_femenino = acu_edad_femenino / con_edad_femenino
    else:
        promedio_femenino = "NO HUBO"

    # D. Nombre de cada participante y porcentaje de los votos qué recibió.  
    #        TOTAL ______ 100% 
    #  10 PERSONA ______ X = 20 * 100 / TOTAL = %  
      
    if con_votos_nacho > 0:
        porcentaje_nacho = con_votos_nacho * 100 / con_votos_total
        msj_porcentaje_nacho = f"Porcentaje de votos de Nacho: {porcentaje_nacho}%"
        # C. Nombre del votante más joven que votó a Nacho.
        msj_votante_mas_joven = f"El votante mas joven que voto a nacho: {votante_mas_joven_nombre} {votante_mas_joven_edad}"
    else:
        msj_porcentaje_nacho = "Porcentaje de votos de Nacho: 0"
        msj_votante_mas_joven = "El votante mas joven que voto a nacho: NO HUBO"
    
    if con_votos_julieta > 0:
        porcentaje_julieta = con_votos_julieta * 100 / con_votos_total
        msj_porcentaje_julieta = f"Porcentaje de votos de Julieta: {porcentaje_julieta}&"
    else:
        msj_porcentaje_julieta = "Porcentaje de votos de Julieta: 0"

    if con_votos_marcos > 0:
        porcentaje_marcos = con_votos_marcos * 100 / con_votos_total
        msj_porcentaje_marcos = f"Porcentaje de votos de Marcos: {porcentaje_marcos}%"
    else:
        msj_porcentaje_marcos = "Porcentaje de votos de Marcos: 0"
    # E. El nombre del participante que ganó el reality (El que tiene más votos)
    if con_votos_marcos > con_votos_nacho and con_votos_marcos > con_nacho_julieta:
        participante_ganador = "El ganador es Marcos"
    elif con_votos_nacho > con_votos_julieta:
        participante_ganador = "El ganador es Nacho"
    else:
        participante_ganador = "El ganador es Julieta"



        
    print(f"El promedio de mujeres que votaron: {promedio_femenino}")
    print(f"Personas entre 25-40 masculinos que votaron a Nacho y Julieta: {con_nacho_julieta}")

    print(msj_porcentaje_nacho)
    print(msj_porcentaje_julieta)
    print(msj_porcentaje_marcos)

    print(msj_votante_mas_joven)
    print(participante_ganador)
  
mostrar()