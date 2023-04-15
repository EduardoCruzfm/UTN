from os import system
system("cls")


from data import lista_bzrp



menu = [".Mostrar temas", "2.Mostrar temas con vistas", "3.Mostrar temas mas vistos", "4.Mostrar    temas menos vistos", "5.Mostrar promedio reproducciones", "6.Salir"]


seguir = True

while seguir == True:
    for opcion in menu:
        print(opcion)
    
    respuesta = int(input("Ingrese una opcion: "))

    match respuesta:
        case 1:
            #B Recorrer la lista imprimiendo por consola el título de cada video
            for i in range(len(lista_bzrp)):
                print(f"{lista_bzrp[i]['title']}")
            
        case 2:
            #C Recorrer la lista imprimiendo por consola el título de cada video junto a la
            # cantidad de reproducciones del mismo

            for tema in lista_bzrp:
                print(f"{tema['title']} - {tema['views']}")
            
        case 3:
            #D Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones
            # (MÁXIMO)

            flag_primero = True
            maxima_views = 0

            for tema in lista_bzrp:
                if flag_primero == True or tema['views'] > maxima_views:
                    maxima_views = tema['views']
                    flag_primero = False

            print(f"Cantidad maxima de reproduccion: {maxima_views}")

            for tema in lista_bzrp:
                if tema['views'] == maxima_views:
                    print(f"{tema['title']}")
            
        case 4:
            #E Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones
            # (MÍNIMO)

            flag_primero = True
            minima_views = 0

            for tema in lista_bzrp:
                if flag_primero == True or tema['views'] < minima_views:
                    minima_views = tema['views']
                    flag_primero = False

            print(f"Cantidad minima de reproduccion: {minima_views}")
            for tema in lista_bzrp:
                if tema['views'] == minima_views:
                    print(f"{tema['title']}")
            
        case 5:
            
            #F Recorrer la lista y determinar la cantidad total de reproducciones del canal
            # (ACUMULADOR)

            acumulador_views = 0

            for tema in lista_bzrp:
                acumulador_views += tema["views"]

            print(f"Sumatoria de reproduciones: {acumulador_views}")

            contar_temas = len(lista_bzrp)
            promedio_views = acumulador_views / contar_temas

            print(f"El promedio de visitas es: {promedio_views}")

        case 6:
            seguir = False


