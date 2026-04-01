num_ejercicio = int(input("Por favor, ingrese el número de ejercicio que desea ejecutar (1-10): "))

match num_ejercicio:
    case 1:
    #Ejercicio 1. Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en 
    #pantalla que diga “Es mayor de edad”. 
        edad = int(input("Por favor, ingrese su edad: "))

        if edad >= 18:
            print("Es mayor de edad.")
    
    case 2:
    #Ejercicio 2.  Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje
    #que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 
        
        nota = int(input("Por favor, ingrese su nota: "))

        if nota >= 6:
            print("Aprobado")
        
        else:
            print("Desaprobado")
    
    case 3:
    #Ejercicio 3. Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje 
    #"Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

        numero = int(input("Por favor, ingrese un número par: "))

        if numero % 2 == 0:
            print("Ha ingresado un número par.")
    
        else:
            print("Por favor, ingrese un número par.")

    case 4:
    #Ejercicio 4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
    #• Niño/a: menor de 12 años.
    #• Adolescente: mayor o igual que 12 años y menor que 18 años.
    #• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    #• Adulto/a: mayor o igual que 30 años. 

        LIMITE_NINIO = 12
        LIMITE_ADOLESCENTE = 18
        LIMITE_JOVEN = 30

        edad = int(input("Por favor ingrese su edad: "))

        print("Pertenece a la categoría: ")

        if 122 >= edad >= 0:
            if edad < LIMITE_NINIO:
                print("Niño/a")
            elif edad < LIMITE_ADOLESCENTE:
                print("Adolescente")
            elif edad < LIMITE_JOVEN:
                print("Adulto/a joven")
            else:
                print("Adulto/a mayor")
        else:
            print("No ha ingresado una edad válida.")
    case 5:
    #Ejercicio 5. Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
    #Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado
    #una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres
        LEN_MAXIMA = 14
        LEN_MINIMA = 8
        contrasenia = input("Por favor, ingrese una contraseña que contenga entre 8 y 14 caracteres: ")

        if LEN_MINIMA <= len(contrasenia) <= LEN_MAXIMA:
            print("Ha ingresado una contraseña correcta.")
        
        else:
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
    
    case 6:
    #Ejercicio 6. Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
    #kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
    #• Menor que 150 kWh: “Consumo bajo”.
    #• Entre 150 y 300 kWh (inclusive): “Consumo medio”.
    #• Mayor que 300 kWh: “Consumo alto”. Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
    #“Considere medidas de ahorro energético”.
        
        LIMITE_BAJO = 150
        LIMITE_MEDIO = 300
        LIMITE_ADICIONAL = 500

        consumo_mensual = int(input("Por favor, ingrese el consumo de energía mensual en kilovatios (kwh): "))

        if consumo_mensual < LIMITE_BAJO:
            print("Consumo bajo")
        elif consumo_mensual <= LIMITE_MEDIO:
            print("Consumo medio")
        else: 
            print("Consumo alto")
            if consumo_mensual > LIMITE_ADICIONAL:
                print("Considere medidas de ahorro energético.")
    
    case 7:
    #Ejercicio 7. Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
    #termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
    #en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla
        
        palabra_frase = input("Por favor, ingrese una palabra o una frase: ")

        if palabra_frase[-1] in ["a","e","i","o","u","A","E","I","O","U"]:

            palabra_frase += "!"
            print(palabra_frase)
        
        else:
            print(palabra_frase)
    
    case 8:
    #Ejercicio 8.  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
    #dependiendo de la opción que desee:
    #1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    #2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    #3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
        
        nombre = input("Por favor, ingrese su nombre: ")

        print("Seleccione una de las siguientes opciones (1, 2 o 3): ")
        print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
        print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
        print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

        opcion = int(input("Opcion deseada: "))

        if opcion == 1:
            print(nombre.upper())
        elif opcion == 2:
            print(nombre.lower())
        elif opcion == 3:
            print(nombre.title())
        else:
            print("La opción ingresada no es válida.")
    
    case 9:
    #Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las
    #siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
    #• Menor que 3: "Muy leve" (imperceptible).
    #• Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    #• Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
    #• Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
    #• Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    #• Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
        LIMITE_MUYLEVE = 3
        LIMITE_LEVE = 4
        LIMITE_MODERADO = 5
        LIMITE_FUERTE = 6
        LIMITE_MUYFUERTE = 7
        
        magnitud_terremoto = int(input("Por favor, ingrese la magnitud de un terremoto según la escala de Richter: "))
        
        if magnitud_terremoto >= 0:
            if magnitud_terremoto < LIMITE_MUYLEVE:
                print("Muy leve (imperceptible)")
            elif magnitud_terremoto < LIMITE_LEVE:
                print("Leve (ligeramente perceptible)")
            elif magnitud_terremoto < LIMITE_MODERADO:
                print("Moderado (sentido por personas, pero generalmente no causa daños)")
            elif magnitud_terremoto < LIMITE_FUERTE:
                print("Fuerte (puede causar daños en estructuras débiles)")
            elif magnitud_terremoto < LIMITE_MUYFUERTE:
                print("Muy Fuerte (puede causar daños significativos)")
            else:
                print("Extremo (puede causar graves daños a gran escala)")
        
        else:
            print("No se permiten números negativos.")
    
    case 10:
    #Ejercicio 10. Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
    #del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el
    #usuario se encuentra en otoño, invierno, primavera o verano.
        hemisferio = input("Por favor, ingrese el hemisferop en que se encuentra (N/S): ")
        mes = int(input("Por favor, ingrese el mes del año (1 al 12): "))
        dia = int(input("Por favor, ingrese el día: "))

        hemisferio = hemisferio.upper()


        if (hemisferio in ("N","S","NORTE","SUR")) and (0 < dia <= 31) and (mes in [1,2,3,4,5,6,7,8,9,10,11,12]):
            print("Usted se encuentra en la estación del año: ")
            if (hemisferio == "N" or hemisferio == "NORTE"):
                if (dia >= 21 and mes == 12) or (1 <= dia <= 31 and mes == 1) or (1 <= dia <= 28 and mes == 2) or (1 <= dia <= 20 and mes == 3):
                    print("Invierno")
                elif (dia >= 21 and mes == 3) or (1 <= dia <= 30 and mes == 4) or (1 <= dia <= 31 and mes == 5) or (1 <= dia <= 20 and mes == 6):
                    print("Primavera")
                elif (21 <= dia <= 30 and mes == 6) or (1 <= dia <= 31 and mes == 7) or (1 <= dia <= 31 and mes == 8) or (1 <= dia <= 20 and mes == 9):
                    print("Verano")
                elif (21 <= dia <= 30 and mes == 9) or (1 <= dia <= 31 and mes == 10) or (1 <= dia <= 30 and mes == 11) or (1 <= dia <= 20 and mes == 12):
                    print("Otoño")
        
            elif (hemisferio == "S" or hemisferio == "SUR"):
                if (dia >= 21 and mes == 12) or (1 <= dia <= 31 and mes == 1) or (1 <= dia <= 28 and mes == 2) or (1 <= dia <= 20 and mes == 3):
                    print("Verano")
                elif (dia >= 21 and mes == 3) or (1 <= dia <= 30 and mes == 4) or (1 <= dia <= 31 and mes == 5) or (1 <= dia <= 20 and mes == 6):
                    print("Otoño")
                elif (21 <= dia <= 30 and mes == 6) or (1 <= dia <= 31 and mes == 7) or (1 <= dia <= 31 and mes == 8) or (1 <= dia <= 20 and mes == 9):
                    print("Invierno")
                elif (21 <= dia <= 30 and mes == 9) or (1 <= dia <= 31 and mes == 10) or (1 <= dia <= 30 and mes == 11) or (1 <= dia <= 20 and mes == 12):
                    print("Primavera")

        else:
            print("Fecha y/o hemisferio inválido/s")