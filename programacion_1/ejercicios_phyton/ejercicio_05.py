'''
Eduardo Cruz DIV B
Ejercicio 05

Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento
de HR dispone de lista de justicieros pero solo tiene información detallada de algunos de
ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista
heroes_info se puedan listar los datos de cada héroe con el siguiente formato:

ID: 1, Codename: Super Girl
Identidad: Kara Zor-El, Origen Krypton
Habilidades: Volar | Fuerza | Velocidad
---------------------------------------
ID: 14, Codename: Power Girl
Identidad: Karen Starr, Origen Krypton
Habilidades: Volar | Fuerza | Congelar
--------------------------------------
ID: 25, Codename: Shazam
Identidad: Billy Baston, Origen Tierra
Habilidades: Volar | Fuerza | Velocidad | Magia
--------------------------------------
ID: 29, Codename: Wonder Woman
Identidad: Diana Pronce, Origen Amazonia
Habilidades: Agilidad | Fuerza | Lazo de la verdad | Escudo
--------------------------------------

TIP: Las habilidades están repetidas, buscá la manera de que en el resultado final no existan
duplicados, que usarías para eso?

'''
from os import system
system("cls")


heroes_info = [
    {
    "Nombre":"Super Girl",
    "ID": 1,
    "Origen": "Kryton",
    "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
    "Identidad": "Kara Zor-El"
    },
    {
    "Nombre":"Shazam",
    "ID": 25,
    "Origen": "Tierra",
    "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
    "Identidad": "Billy Batson"
    },
    {
    "Nombre":"Power Girl",
    "ID": 14,
    "Origen": "Kryton",
    "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
    "Identidad": "Karen Starr"
    },
    {
    "Nombre":"Wonder Woman",
    "ID": 29,
    "Origen": "Amazonia",
    "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
    "Identidad": "Diana Prince"
    }
]

'''
--------------------------------------
ID: 29, Codename: Wonder Woman
Identidad: Diana Pronce, Origen Amazonia
Habilidades: Agilidad | Fuerza | Lazo de la verdad | Escudo
--------------------------------------
'''

for heroe in heroes_info:
    ID = heroe["ID"]
    codename = heroe["Nombre"]
    identidad = heroe["Identidad"]
    origen = heroe["Origen"]
    habilidades = set(heroe["Habilidades"])
    habilidad = " | ".join(habilidades)
    # print(heroe["ID"])
    # print(f"{ID}-{Codename}")
    print(f" ID: {ID}, Codename: {codename}\n Identidad: {identidad}, Origen: {origen}\n Habilidades: {habilidad}")

    print("\n -------------------------------------- \n ")

    # for habilidad in habilidades:
    #     poder = []
    #     poder.append(habilidad)

    #     print(f" {'|'.join(habilidad)}")

        