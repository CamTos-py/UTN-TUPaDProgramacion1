#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

CUPOS_LUNES = 4 
CUPOS_MARTES = 3            #Definición de constantes para cupos fijos en cada día

lunes1 = ""
lunes2 = ""                 #Inicialización de la svariables que contendran los turnos de cada día. Iniciadas con "" ("vacio")
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


nombre = input("Ingrese su nombre: ")

while not (nombre.isalpha()):                       #Validación con .isalpha() en bucle while
    print("El nombre solo puede contener letras")
    nombre = input("Ingrese su nombre: ")

while True:                                 #Despliegue del menú de opciones
    print("\nMenú de opciones:")
    print("   1. Reservar turno")
    print("   2. Cancelar turno")
    print("   3. Ver agenda del día")
    print("   4. Ver resumen general")
    print("   5. Cerrar sistema")
    opcion_menu = input("Opción: ")

    if not (opcion_menu.isdigit()):                 #Validación con .isdigit() en bucl while
        print("Error. Solo se permiten numeros")
        continue

    opcion_menu = int(opcion_menu)

    if opcion_menu < 1 or opcion_menu > 5:           #Validación del rango
        print("Error. Rango incorrecto")
        continue
#Opcion 1 - Reservar turno
    if opcion_menu == 1:
        print("\n1. Reservar turno")
        print("Seleccione el día:\n1. Lunes\n2. Martes")

        opcion_dia_1 = input("Opción: ")

        while not (opcion_dia_1.isdigit()):             #Validación con .isdigit() en bucl while
            print("Error. Solo se permiten numeros")
            opcion_dia_1 = input("Opción: ")
        
        opcion_dia_1 = int(opcion_dia_1)

        while opcion_dia_1 < 1 or opcion_dia_1 > 2:     #Validación del rango
            print("Error. Rango incorrecto")
            opcion_dia_1 = input("Opción: ")
            opcion_dia_1 = int(opcion_dia_1)
        
        if opcion_dia_1 == 1:
            print("\nOpción elegida: Lunes")

            nombre_reserva = input("Ingrese su nombre: ").title()  #Uso funcion .title() para que los nombres cohincidan

            while not (nombre_reserva.isalpha()):                   #Validación con .isalpha() en bucl while
                print("Error. Solo se permiten letras")
                nombre_reserva = input("Ingrese su nombre: ").title()
            
            if (nombre_reserva == lunes1 or nombre_reserva == lunes2 or nombre_reserva == lunes3 or nombre_reserva == lunes4):
                print("Ese nombre ya tiene turno")      #Condición para determinar si ese nombre ya tiene turnoasignado

            elif lunes1 == "":                          #Condicionales para determinar cuál es el primer turno disponible
                lunes1 = nombre_reserva
                print("Turno 1 - Asignado con éxito")

            elif lunes2 == "":
                lunes2 = nombre_reserva
                print("Turno 2 - Asignado con éxito")

            elif lunes3 == "":
                lunes3 = nombre_reserva
                print("Turno 3 - Asignado con éxito")

            elif lunes4 == "":
                lunes4 = nombre_reserva
                print("Turno 4 - Asignado con éxito")
            
            else:
                print("No hay cupos disponibles")

        elif opcion_dia_1 == 2:                          #Misma lógica aplicada a la opción 2
            print("\nOpción elegida: Martes")

            nombre_reserva = input("Ingrese su nombre: ").title()

            while not (nombre_reserva.isalpha()):
                print("Error. Solo se permiten letras")
                nombre_reserva = input("Ingrese su nombre: ")
            
            if (nombre_reserva == martes1 or nombre_reserva == martes2 or nombre_reserva == martes3):
                print("Ese nombre ya tiene turno")

            elif martes1 == "":
                martes1 = nombre_reserva
                print("Turno 1 - Asignado con éxito")

            elif martes2 == "":
                martes2 = nombre_reserva
                print("Turno 2 - Asignado con éxito")

            elif martes3 == "":
                martes3 = nombre_reserva
                print("Turno 3 - Asignado con éxito")
            
            else:
                print("No hay cupos disponibles")
#Opción 2 - Cancelar turno
    if opcion_menu == 2:
        print("\n2. Cancelar turno")
        print("Seleccione el día:\n1. Lunes\n2. Martes")

        opcion_dia_2 = input("Opción: ")

        while not (opcion_dia_2.isdigit()):     #Validación con .isdigit() en bucle while
            print("Error. Solo se permiten numeros")
            opcion_dia_1 = input("Opción: ")
        
        opcion_dia_2 = int(opcion_dia_2)

        while opcion_dia_2 < 1 or opcion_dia_2 > 2:     #Validación de rango
            print("Error. Rango incorrecto")
            opcion_dia_2 = input("Opción: ")
            opcion_dia_2 = int(opcion_dia_2)

        if opcion_dia_2 == 1:

            cohincidencia = False           #Inicialización de variable <cohincidencia> 

            print("\nOpción elegida: Lunes")

            nombre_reserva = input("Ingrese su nombre: ").title()

            while not (nombre_reserva.isalpha()):               #Validación con .isalpha() en bucle while
                print("Error. Solo se permiten letras")
                nombre_reserva = input("Ingrese su nombre: ").title()
            
            if nombre_reserva == lunes1:            #Condicionales que determinan si el nombre ingresado cohincide con el contenido de alguna de las variables, de ser así vuelve a la variable del turno a "" ("vacío")
                lunes1 = ""
                cohincidencia = True
            
            elif nombre_reserva == lunes2:
                lunes2 = ""
                cohincidencia = True

            elif nombre_reserva == lunes3:
                lunes3 = ""
                cohincidencia = True

            elif nombre_reserva == lunes4:
                lunes4 = ""
                cohincidencia = True

            if cohincidencia:
                print("Turno cancelado con éxito")

            else:
                print("No se encontró ese turno")

        elif opcion_dia_2 == 2:                             #Misma lógica aplicada a la opción 2
            print("\nOpción elegida: Martes")
        
            nombre_reserva = input("Ingrese su nombre: ").title()

            while not (nombre_reserva.isalpha()):
                print("Error. Solo se permiten letras")
                nombre_reserva = input("Ingrese su nombre: ")
            
            cohincidencia = True

            if nombre_reserva == martes1:
                martes1 = ""
                cohincidencia = True
            
            elif nombre_reserva == martes2:
                martes2 = ""
                cohincidencia = True

            elif nombre_reserva == martes3:
                martes3 = ""
                cohincidencia = True
            
            if cohincidencia:
                print("Turno cancelado con éxito")
                
            else:
                print("No se encontró ese turno")
#Opción 3 - Agenda de turnos
    if opcion_menu == 3:
        print("\n3. Agenda de turnos")
        print("\nLunes")
        print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")        #Uso de condicional ternario. Si lunes es distinto a "" (imprime ocupado), sino (imprime libre)
        print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
        print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
        print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        print("\nMartes")
        print("Turno 1:", martes1 if martes1 != "" else "(libre)")
        print("Turno 2:", martes2 if martes2!= "" else "(libre)")
        print("Turno 3:", martes3 if martes3 != "" else "(libre)")
#Opción 4 - Resumen general
    elif opcion_menu == 4:
        print("\n4. Resumen general")

        ocupados_lunes = 0        #Inicialización de la variable que va a funcionar como contador para la cantidad de turnos ocupados

        if lunes1 != "":           #Condicional, si la variable no está vacía, suma 1 a la variable <ocupados_lunes>
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes +=1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes +=1
        
        ocupados_martes = 0         #Misma lógica 

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes +=1
        if martes3 != "":
            ocupados_martes += 1
        print(f"\nResumen General:")                                #Uso de constantes para restarles los turnos ocupados
        print(f"Lunes:\nOcupados: {ocupados_lunes} turnos\nLibres: {CUPOS_LUNES - ocupados_lunes} turnos")
        print(f"Martes:\nOcupados: {ocupados_martes} turnos\nLibres: {CUPOS_MARTES - ocupados_martes} turnos")

        if ocupados_lunes > ocupados_martes:                        #Uso de condicional compuesto para determinar que día tiene más turnos, o un empate
            print("Mayor cantidad de turnos el dia: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Mayor cantidad de turnos el dia: Martes")

        elif ocupados_lunes == ocupados_martes:
            print("MMisma cantidad de turnos en ambos días")
#Opcion 5 - Cierre
    elif opcion_menu == 5:
        print("5. Cerrar sistema\nCerrando...")
        break                                       #Uso de break para detener el programa.