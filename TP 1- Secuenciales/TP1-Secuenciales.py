ejercicio = int(input("Ingrese el número de ejercicio que desee probar (1 al 10): "))

match ejercicio:
    case 1:
        #1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

        print ("Hola Mundo!")
    
    case 2:
        #2. Crear un programa que pida al usuario su nombre e imprima 
        #por pantalla un saludo usando el nombre ingresado. Por ejemplo:
        #si el usuario ingresa “Marcos”, el programa debe imprimir por 
        #pantalla “Hola Marcos!”. Consejo: esto será más sencillo si 
        #utilizas print(f…) para realizar la impresión por pantalla.

        nombre = input ("Por favor, ingrese su nombre: ")

        print (f"Hola {nombre}!")
    
    case 3:
        #3. Crear un programa que pida al usuario su nombre, apellido, edad y 
        #lugar de residencia e imprima por pantalla una oración con los datos
        #ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, 
        #“30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez,
        #tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si
        #utilizas print(f…) para realizar la impresión por pantalla

        nombre = input("Por favor, ingrese su nombre: ")

        apellido = input("Por favor, ingrese su apellido: ")

        edad = input("Por favor, ingrese su edad: ")

        residencia = input("Por último, ingrese su lugar de residencia: ")

        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

    case 4:
        #4. Crear un programa que pida al usuario el radio de un círculo e imprima
        #por pantalla su área y su perímetro.

        radio = float(input("Por favor, ingrese el radio del círculo: "))

        pi = 3.14159

        area = pi * (radio**2)
        perimetro = 2 * pi * radio

        print(f"El área del círculo es: {area}.")
        print(f"El perímetro del círculo es: {perimetro}.")
    
    case 5:
        #5. Crear un programa que pida al usuario una cantidad de segundos e imprima
        #por pantalla a cuántas horas equivale.

        segundos = int(input("Ingrese una cantidad de segundos: "))

        horas = segundos / 60

        print(f"{segundos} segundos equivalen a {horas} horas.")
    
    case 6:
        #6. Crear un programa que pida al usuario un número e imprima por pantalla
        #la tabla de multiplicar de dicho número.

        numero = int(input("Por favor ingrese un número para ver su tabla de multiplicar: "))

        print("Tabla de multiplicar")
        print(f"{numero}x1={numero}\n{numero}x2={numero*2}\n{numero}x3={numero*3}\n{numero}x4={numero*4}\n{numero}x5={numero*5}\n{numero}x6={numero*6}\n{numero}x7={numero*7}\n{numero}x8={numero*8}\n{numero}x9={numero*9}\n{numero}x10={numero*10}")

    case 7:
        #7. Crear un programa que pida al usuario dos números enteros distintos 
        #del 0 y muestre por pantalla el resultado de sumarlos, dividirlos,
        #multiplicarlos y restarlos.

        valor_uno = int(input("Por favor, ingrese dos números enteros distintos a 0.\nIngrese el primer número: "))
        valor_dos = int(input("Ingrese el segundo número: "))

        print(f"Suma:\n{valor_uno}+{valor_dos}={valor_uno+valor_dos}")
        print(f"Resta:\n{valor_uno}-{valor_dos}={valor_uno-valor_dos}")
        print(f"Multiplicación:\n{valor_uno}x{valor_dos}={valor_uno*valor_dos}")
        print(f"División:\n{valor_uno}÷{valor_dos}={valor_uno/valor_dos}")
    
    case 8:
        #8. Crear un programa que pida al usuario su altura y su peso e imprima por
        #pantalla su índice de masa corporal. Tener en cuenta que el índice de 
        #masa corporal se calcula del siguiente modo: IMC= peso(kg) / (altura(mts.))**2

        altura = float(input("Por favor, ingrese su altura en metros: "))
        peso = int(input("Por favor, ingrese su peso en kg: "))

        print(f"Su índice de masa corporal(IMC) es de: {peso/(altura**2)}")

    case 9:
        #9. Crear un programa que pida al usuario una temperatura en grados Celsius
        #e imprima por pantalla su equivalente en grados Fahrenheit.
        #Tener en cuenta la siguiente equivalencia: F=(C°×9/5)+32

        temperatura_celcius = int(input("Por favor, ingrese una temperatura en grados celcius: "))

        print(f"El equivalente de {temperatura_celcius}°C en grados farenheit es de: {(temperatura_celcius*(9/5)+32)}°F")

    case 10:
        #10. Crear un programa que pida al usuario 3 números e imprima por pantalla
        #el promedio de dichos números.
        
        print("Para ver el promedio de tres números:")

        valor_uno = int(input("Por favor, ingrese el primer número: "))
        valor_dos = int(input("Por favor, ingrese el segundo número: "))
        valor_tres = int(input("Por favor, ingrese el tercer número: "))

        promedio = (valor_uno + valor_dos + valor_tres)/3

        print(f"El primedio de los valores ingresados ({valor_uno}, {valor_dos} y {valor_tres}) es de:\n{promedio}")