'''
3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
 edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
 cantidad de carreras ganadas (no pueden ser números negativos)
 número del vehículo (no puede ser un número negativo)
se necesita saber:
*Nacionalidad del piloto más joven.
*Cantidad de vehículos con número par.
*Nombre del piloto con menos victorias y el número de auto impar.
*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
*Nombre del piloto más joven con más victorias.
*Nacionalidad del piloto más veterano con menos victorias.
*Promedio de edad de los pilotos que tiene un vehículo con número par.
'''


nombre_piloto = input("ingtrese nombre")

edad_piloto = int(input("Ingrese edad"))
while edad_piloto > 17:
    edad_piloto = input("ERROR: Reingrese edad")

nacionalidad_piloto = input("ingrese nacionalidad:(argentino, ingles, frances, brasilero, estadounidense)")
while nacionalidad_piloto != "argentino" and nacionalidad_piloto != "ingles" and nacionalidad_piloto != "frances" and nacionalidad_piloto != "brasilero" and nacionalidad_piloto != "estadounidense":
    nacionalidad_piloto = input("ERROR: Reingrese nacionalidad:(argentino, ingles, frances, brasilero, estadounidense)")

cant_de_carreras = int(input("Ingrese cantidad de carrearas"))
while cant_de_carreras > 0:
    cant_de_carreras = input("ERROR: Reingresecantidad de carrearas")

numero_de_vehiculo = int(input("Ingrese cantidad de vehiculos"))
while numero_de_vehiculo > 0:
    numero_de_vehiculo = int(input("ERROR: Reingrese cantidad de vehiculos"))

ban_piloto_mas_joven = True

if ban_piloto_mas_joven == True:
    piloto_mas_joven_nombre = nombre_piloto
    piloto_mas_joven_edad = edad_piloto
    ban_piloto_mas_joven == False

elif edad_piloto < piloto_mas_joven_edad:
    piloto_mas_joven_nombre = nombre_piloto
    piloto_mas_joven_edad = edad_piloto

#Cantidad de vehículos con número par.
cantidad_vehiculos_par = 0

if numero_de_vehiculo%2 == 0:
    cantidad_vehiculos_par += 1

#Nombre del piloto con menos victorias y el número de auto impar.

# 17.	Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.