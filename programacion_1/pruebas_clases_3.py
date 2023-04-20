def sumar_numeros(primer_numero:int, segundo_numero:int)->int: #IMPLEMENTACION DE LA FUNCION
   
    suma = primer_numero + segundo_numero
    return suma

def resta_numero(primer_numero:int, segundo_numero:int)->int:
    
    resta = primer_numero - segundo_numero 
    return resta

def multiplicar_numero(primer_numero:int, segundo_numero:int)->int:
    
    multiplicar = primer_numero  * segundo_numero
    return multiplicar

def dividir_numero(primer_numero:int, segundo_numero:int):
    division = None
    if segundo_numero != 0:
        division = primer_numero / segundo_numero

    return division

while True:
    opcion = int(input("1.Ingrese numeros\n. Resta\n3. Multiplicar \n4. Dividir\n5. Sumar\n6. Salir\n Ingrese opcion:  "))
    match opcion:
        case 1:
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese un numero: "))
        case 2:
            resultado = resta_numero(x,y)
            print(f"El resultado de la resta es: {resultado}")
        case 3: 
            resultado = multiplicar_numero(x,y)
            print(f"El resultado de la multiplicaion es: {resultado}")
        case 4:
            resultado = dividir_numero(x,y)
            if resultado != 0:
                print(f"El resultado de la divicion es: {resultado}")
            else:
                print("Error no se puede divir por cero")
        case 5:
            resultado = suma_numero(x,y)
            print(f"El resultado de la suma es: {resultado}")
        case 6:
            break
