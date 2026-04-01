#Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

anti_spam = 0
boveda = False

nombre_agente = input("Ingrese su nombre, agente: ")   #Validación nombre agente con .isalpha()
while not (nombre_agente.isalpha()):
    print("\nEl nombre solo puede contener letras")
    nombre_agente = input("Ingrese su nombre, agente: ")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    if alarma == True and tiempo <= 3 and boveda == False:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("¡La Alarma se ha activado!\nSistema bloqueado\n\nDerrota")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
    
    
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"\nEnergía: {energia}   Tiempo: {tiempo}   Cerraduras abiertas: {cerraduras_abiertas}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nMenú:")
    print("1. Forzar cerradura (costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
    print("3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")

    opcion_menu = input("Opción: ")

    while not (opcion_menu.isdigit()):     #Validación opción con .isdigit()
        print("\nElija una opción numérica correcta (1-3)")
        opcion_menu = input("Opción: ")

    opcion_menu = int(opcion_menu)

    if opcion_menu < 1 or opcion_menu > 3:
        print("\nNúmero ingresado fuera del rango (1-3)")
        continue

    if opcion_menu == 2 or opcion_menu == 3:   #Reseteo del anti spam
        anti_spam = 0

    if opcion_menu == 1:        #Opción 1 - Forzar
        anti_spam += 1
        
        energia -= 20
        tiempo -= 2
        cerraduras_abiertas += 1

        print("\nForzando cerradura...")

        if anti_spam == 3 :
            print("\nLa cerradura se trabó. Alarma activada")
            alarma = True
            anti_spam = 0
            continue
                
                        
        if energia < 40:        #Riesgo de alarma
            print("\n¡Riesgo de alarma! - Energía por debajo de 40")
            
            validacion = input("Ingrese un número (1-3): ")
                
            while not (validacion.isdigit()):
                print("\nElija una opción numérica correcta (1-3)")
                validacion = input("Ingrese un número (1-3): ")

            validacion = int(validacion)

            while validacion < 1 or validacion > 3:     #Validación con bucle while con .isdigit()
                    print("\nNúmero ingresado fuera del rango (1-3)")
                    validacion = input("Ingrese un número (1-3): ")
                
            match validacion:
                case 1: 
                    if alarma == False:
                        cerraduras_abiertas += 1
                            
                case 2:
                    if alarma == False:
                        cerraduras_abiertas += 1
                            
                case 3:
                    print("\nAlarma activada")
                    alarma = True
                                                
    elif opcion_menu == 2:
        energia -= 10
        tiempo -= 3

        print("\nHackeando sistema... (costo: -10 energía, -3 tiempo)")

        for i in range (1,5):
            codigo_parcial += "X"
            print(f"Paso {i} completado")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("< Cerradura abierta >")

        print(f"{codigo_parcial}")
        print("_ _ _ _ _ _ _ _")
    #OPCIÓN 3 - DESCANSAR 
    elif opcion_menu == 3:
        print("\nDescansando... ")
        print("+15 energía\n")

        energia += 15
        if energia > 100:
            energia = 100
        
        tiempo -= 1
        
        if alarma  == True :
            energia -= 10
            print("¡Oh no! La alarma esta encendida\n-10 de energía")
        
    #POSIBLES FINALES  
    if cerraduras_abiertas == 3:
            print("*************************************")
            print("¡Victoria! \nLa Bóveda se ha abierto")
            print("*************************************")
            break
    
    if energia <= 0 or tiempo <= 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Derrota. No haz logrado abrir la bóveda a tiempo")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break