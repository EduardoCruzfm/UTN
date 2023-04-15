'''
Eduardo Cruz
Ejercicio 02
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”
'''
from os import system
system("cls")

numero_ingresado = int(input("ingrese un numero entre 1-8:  "))
while numero_ingresado < 1 or numero_ingresado > 8:
    numero_ingresado = int(input("ERROR: Regla de estilo inexistente reingrese:  "))

reglas_de_estilo = {
    1 : "Sentido [Codigo que pueda leerse con facilidad]",
    2 : "PEP [información a la comunidad de Python]",
    3 : "PEP8 [Ayudar a escribir código más legible]",
    4 : "Indentado [Python no usa {} para designar bloques de código]",
    5 : "Tamaño maximo linea [Limitar el tamaño de cada línea]",
    6 : "Lineas en blanco [Mejora la legibilidad del código,]",
    7 : "Comentarios [Actualizar los comentarios para evitar crear inconsistencias]",
    8 : "Nombres [Uso de snake_case]"
}

print(reglas_de_estilo.get(numero_ingresado))
