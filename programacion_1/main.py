"""This is the main module of the project."""
#pylint: disable=invalid-name
numero_entero = 0
numero_entero = input("ingrese un numero")

print(type(numero_entero))

print("El numero ingresado es: ", numero_entero)


######################################
# CLASE 3
#COMPLEJOS (SON AQUELLOS QUE TIENEN UNA PARTE REAL Y OTRA PARTE IMAGONARIA)

c = 3 + 5j
print(c) #-> (3+5j)
print(c.real) #-> (3.0)
print(c.imag) #-> (5.0)
print(type(c)) #-> <class 'complex>





#LISTAS
# Aplica para valores sueltos, lisat de numeros, imagenes
lista = [1, "hola", 3.67]
print(type(lista)) # <class 'list'>
print(lista[1])     # hola
lista[1] = "chau"
print(lista[1])  # chau // pisamos su valor en esa posicion

#TUPLAS SON SIMILARES A LAS LISTAS PERO SON INMUTABLES(NO SE PUEDEN CAMBIAR) -> SOLO LECTURA
# Aplica para set de valore que son inmutables, que no lo tengo que cambiar que son CONSTANTES 
# PARECE QE SE LE PUEDE AGREGAR DATOS, NO MODIFICAR LOS QUE ESTAN

lista =  tuple([1, "hola", 3.67])
print(type(lista)) # <class 'list'>
print(lista[1])     # hola

# lista[1] = "chau"
print(lista[1])  # object does not support item assignment (ERROR)

#DICCIONARIOS  (Key : Value) CLAVE-VALOR
# Aplica para valores de un alunmo, empleado, algo que esos datos tenga una relacion estrecha , etc

diccionario = {'nombre' : 'Juan', 'edad' : 21}
print(diccionario['nombre']) # Juan
print(diccionario['edad']) # 21

#SET ES COMO UNA LISTA QUE NO TIENE ELEMENTOS DUPLICADOS, SI CONVIERTO UNA LISAT CON 
#ELEMETOS REPETIDOS SE LOS SACA

s = {2, 4, 7, 1, 8, 1}
print(s) # {1, 2, 4, 7, 8}
print(type(s)) # <class 'set'>


lista = [1 , 3 , 6, 3, 2, 1]
s = set(lista)
print(s)        # {1 , 2, 3, 6}
print(type(s))  # <class 'set>

################################################

#Pruebas

lista = [1,2,3,4,5,6,7,8,9]
print(lista) # muestra el cuarto index 0,1,2,"3"
print(lista[0:3]) # DESDE INDEX 0 HASTA EL 3 [DESDE:HASTA] D: INCLUSIVO / H:EXCLUSIVO (LLEGA AL INDEX 4 Y LO EXCLIYE)
print(lista[3:5]) # MUESTRA EL 4,5

acumulador = 0
contador = 0
for i in range(len(lista)): # len devuelve la cantidad que tenga la lista
    print(lista[i]) # MUESTRA TODA LA LISTA
    
    acumulador = acumulador + lista[i]
    if lista[i] == 5: #CUANTAS VECES ESTA EL 5 EN EL LOOP
        contador += 1

    print(acumulador) #MUESTRA LA SUMA DE LOS ELEMENTOS DE LA LISTA
    print(contador)

    lista.append(100) #AGREGA ESTE ELEMENTO ALA LISTA COMO UN PUSH DE JS
    lista.append(55)
    print(lista) # MUESTRA LA LISTA CON 100 55 AGREGADOS

    lista.insert(2,999) #INSETA UN VALOR EN LA POSICION 2 EL ELEMENTO 999 Y CORRE ALA DERECHA EL VALOR ANTERIOR 
    print(lista)

    lista.extend([999,888,777]) #SE PARA AL FINAL DE LA LISTA Y AGREGA ESTOS VALORES(PIDE UNA NUEVA LISTA ENTRE())
    print(lista)

    lista.remove(8) # ELIMINA ESE VALOR DE LA LISTA
    print(lista)

    print(lista.index(999)) # ME MUESTRA LA 1ERA OCURRENCIA DE LA POSICION DEL VALOR ACA DA 2

#EMULA A UN FORECH

for numero in lista:
    print(numero)

#########

mi_diccionario = {}

print(type(mi_diccionario)) #<class list>

mi_diccionario["Nombre"] = "Juan" #AGREGAMOS S UNO DATO EN EL DICCIONARIO
print(mi_diccionario["Nombre"]) # DEVUELVE Juan

mi_diccionario["Edad"] = 25
print(mi_diccionario["Edad"]) #DEVUELVE 25

print(mi_diccionario["Nombre"]) #DEVUELVE JUAN

print(mi_diccionario) #DEVUELVE TODO NOMBRE Y EDAD CON VALOR

otro_diccionario = {"Nombre" : "Luis" , "Edad" : 32}
print(otro_diccionario)

for key in otro_diccionario:
    print(key) #----> DEVUELVE LAS CLAVES NOMBRE, EDAD

for valor in otro_diccionario.values():
    print(f"{valor}") #  DEVUELVE JUAN , 32/ PERO PIERDO REFERENCIA ALA KEY

for key in otro_diccionario:
    print(f"{otro_diccionario}") 

##########################

for i in range(len(lista)):            # CON ESTE TIPO DE FOR PODEMOS MODIFICAR LA LISTA
    print(f"{i+1}->{lista[i]}")        # AGREGAR ELEMENTOS O MODOFICAR LA LISTA

for numero in lista:                    # CON ESTE FOR LA LISTA ES INMUTABLE 
    print(numero)                       # NO SE PUEDN MOFIFICAR

#########

#LISTAS PARALELAS

CANTIDAD_ALUMNOS = 3
lista_nombre = []
lista_apellidos = []


for i in range(CANTIDAD_ALUMNOS):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")

    lista_nombre.append(nombre) #AGREGA NOMBRE ALA LISTA DE NOMBRE
    lista_apellidos.append(apellido) #AGREGA APELLIDO ALA LISTA DE APELLIDO

for i in range(CANTIDAD_ALUMNOS):
    #MUESTRA AMBAS LISTAS PARALELAMENTE CON ORDEN DE LA POSICON I
    print(f"{i+1}) Nombre: {lista_nombre[i]} - Apellido: {lista_apellidos[i]}") 
     

###########################

#DICCIONARIOS /UNA LISTA CON DICCIONARIOS

lista_alumnos = [ #-> LISTA
    {"Nombre" : "Juan", "Apellido" : "Ruiz" ,"Edad" : 25},   #POSICION 0  ->DICCIONARIO
    {"Nombre" : "Luis", "Apellido" : "Perez" ,"Edad" : 36},   #POSICION 1  ->DICCIONARIO
    {"Nombre" : "Maria", "Apellido" : "Gomez" , "Edad" : 23}   #POSICION 2  ->DICCIONARIO
]

#CARGAR UNA LISTA

CANTIDAD_ALUMNOS = 3
lista_alumnos = []

for i in range(CANTIDAD_ALUMNOS):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))

    un_alumno = {}      #EN CADA ITERACION CREO UN ALUMONO CON NOMBRE/APELLIDO/EDAD
    un_alumno["Nombre"] = nombre
    un_alumno["Apellido"] = apellido
    un_alumno["Edad"] = edad

    lista_alumnos.append(un_alumno) #LE AGREGO EL DICC un_alumno A lista_alumnos []

lista_alumnos = [       #LISTA HARCODEADA
    {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad' : 25},
    {'Nombre': 'Luis', 'Apellido': 'Gomes', 'Edad' : 64},
    {'Nombre': 'Maria', 'Apellido': 'Ruiz', 'Edad' : 36}
]

#RECORRER LA LISTA, SOLO MOSTRAR lista_alumnos []

for alumno in lista_alumnos: # EN CADA ITERACION ME ROBO UN ALUMNO
    apellido = alumno['Apellido']
    nombre = alumno['Nombre']
    edad = alumno['Edad']

    if edad > 30: #SI QUEREMOS QUE SOLO MUESTRE MAYORES DE 30 DE LA LISTA
        print(f"{apellido}-{nombre}-{edad}") #DESARMO EL DICIONARIO Y LO MUESTRO

#MAS REDUCIDO EL CODIGO SERIA

for alumno in lista_alumnos: # EN CADA ITERACION ME ROBO UN ALUMNO
  
    edad = alumno['Edad']

    if edad > 30: #SI QUEREMOS QUE SOLO MUESTRE MAYORES DE 30 DE LA LISTA
        print(f"{alumno['Apellido']}-{alumno['Nombre']}-{edad}")

#################################



    