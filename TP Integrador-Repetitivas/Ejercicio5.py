#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

#Inicialización de variables
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_base = 15
danio_base_enemigo = 12
turno_gladiador = True

#Entrada de datos por parte del usuario
nombre_gladiador = input("--- BIENVENIDO A LA ARENA ---\n\nNombre del Gladiador: ")

while not (nombre_gladiador.isalpha()):   #Validación con .isalpha() en bucle while
    nombre_gladiador = input("Error: Solo se permiten letras\nIngrese su nombre: ")   

print("\n~~~~~~~~~~~ INICIO DEL COMBATE ~~~~~~~~~~~~~~~")
while vida_gladiador > 0 and vida_enemigo > 0:  #Uso de bucle while para que el juego continue hasta que no se cumpla la condición
    
    
    print("Gladiador         VS                  Enemigo")
    print(f"HP: {vida_gladiador}                               HP: {vida_enemigo}\nPociones: {pociones_vida}\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Tu turno\n")
    print("\nMenú:")                #Impresión en pantalla del estado del Gladiador y del Enemigo, y despliegue del menú de opciones
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion_menu = input("\nOpción: ")

    while not (opcion_menu.isdigit()):      #Validación con .isdigit() en bucle while
        opcion_menu = input("Error.Solo se permiten números\nOpción: ")

    opcion_menu = int(opcion_menu)  #Conversión de la variable de str a int

    while opcion_menu < 1 or opcion_menu > 3:  #Validación del rango ingresado por el usuario sobre las opciones del menú 
            opcion_menu = int(input("Error. Fuera de rango\nOpción: "))

#Opción 1 - Ataque pesado
    if opcion_menu == 1:        #Uso del condicional si la opción elegida es la 1

        if vida_enemigo < 20:      #Uso del condicional para definir el "Golpe Crítico"
            vida_enemigo -= danio_base * 1.5

            print("Golpe crítico")
            print(f"¡Atacaste al enemigo por {danio_base*1.5} puntos de daño!")
            
        else:                       #Si la condición del if no se cumple, es decir la vida_enemigo > 20, se ejecuta lo siguiente, es decirr el daño base
            vida_enemigo -= danio_base

            print(f"¡Atacaste al enemigo por {danio_base} puntos de daño!")

#Opción 2 - Ráfaga Veloz
    elif opcion_menu == 2:
        print("\nRáfaga Veloz")

        for i in range(3):              #Uso de bucle for para establecer 3 iteraciones
            vida_enemigo -= 5           #Por cada iteración vida_enemigo -= 5. 15 puntos en total
            print(">>>> Golpe conectado por 5 de daño  >>>>")

#Opción 3 - Curar 
    else:                               #Debido a que hay una validación previa del rango, si la opcion ingresada no es ni 1 ni 2, la única opción posible es el 3. Por esto else
        if pociones_vida > 0:           #Uso del condicional para establecer la función de curación. Si quedan pociones, es decir pociones_vida > 0, entonces se ejecuta lo siguiente
            vida_gladiador += 30
            pociones_vida -= 1

            print("\nCurando...")
            
        else:                           #En caso que la variable pociones_vida == 0. No se genera ninguna acción, m{as que informar al usuario que no le quedan pociones.
            print("¡No te quedan pociones!")
            print("\n>> Pierdes el turno")

    vida_gladiador -= danio_base_enemigo  #Como el enemigo ataca automaticamente luego de nuestra jugada, se le resta a la variable vida_gladiador el daño base del enemigo
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Turno del enemigo\n")
    print(f">>>>> ¡El enemigo te atacó por {danio_base_enemigo} puntos de daño! <<<<<")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\n        === NUEVO TURNO ===")

if vida_gladiador > 0:                  #Condicional que se ejecuta si la condición del while principal de arriba da False, es decir not (vida_gladiador > 0 and vida_enemigo > 0)
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.") #Si la variable vida_gladiador > 0, gana, ya que la otra opción posible para que la condicion (vida_gladiador > 0 and vida_enemigo > 0) de falsa es que vida_enemigo <= 0

elif vida_gladiador <= 0:               #Si, en caso contrario la vida_gladiador <= 0, el usuario pierde la partida
    print("\nDERROTA. Has caído en combate")

    #FIN DEL PROGRAMA