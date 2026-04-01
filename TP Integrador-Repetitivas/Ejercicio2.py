#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"     #Definir credenciales fijas en el código
clave_correcta = "python123" 

opcion_menu = ""                #Variable vacía para almacenar luego la opción del menú de opciones              


for intentos in range (1,4):    #Uso de bucl for para cantidad de iteraciones determinadas (3 en este caso)
    usuario_ingresado = input(f"Intento {intentos}/3\nUsuario: ")  #Entrada de datos por parte del usuario, se ve el n° de intentos. Por eso inicié el rango en 1 y no en 0
    clave_ingresada = input("Clave: ") 

    if clave_ingresada == clave_correcta and usuario_ingresado == usuario_correcto:   #Uso del condicional y operadores lógicos, se ejecuta en caso que ambas variables coincidan con los datos correctos
        print("Acceso concedido")
        break                                   #Uso de la palabra reservada break para salir del bucle cuando los datos ingresados coincidan con las credenciales 

    else:                                                                             #Condicional compuesto 
        print("Error: credenciales inválidas")

if clave_ingresada == clave_correcta and usuario_ingresado == usuario_correcto:    #Uso de condicional y operador lógico, si el acceso se concede, se muestra el menú de opciones
    print("\nMenú de opciones: ")
    print("1. Estado de inscripción  2. Cambiar clave  3. Mensaje  4. Salir")
    while True:                             #Uso de bucle para menú de opciones, se ejecuta mientras la condicion del if de arriba se cumpla.
        opcion_menu = input("Opción: ")     

        if not (opcion_menu.isdigit()):   #Validación si la variable <opcion_menu> NO es un digito con el uso de .isdigit() con bucle while
            opcion_menu = print("Error, ingrese un numero válido")      
            continue                      #Uso de palabra reservada 'continue' para inicializar de nuevo el bucle, ignorando cuando no se ingresa un dígito
        
        opcion_menu = int(opcion_menu)   #Una vez determinado que lo ingresado es un dígito, transformamos de un str(cadena) a un int(entero)

        if opcion_menu < 1 or opcion_menu > 4:       #Uso de bucle while para delimitar rango de opciones numericas
            print("Error, opcion fuera de rango.")
            continue                                  #En caso de estar fuera de rango, inicia el bucle denuevo

        if opcion_menu >=1 and opcion_menu <= 4:       #Condicional si se cumple que el dato ingresado es una opción numérica dntro del rango (1-4)
            match opcion_menu:                         #Elegí el uso de la estructura match case, por su sintaxis. Pero tambíen podría hacerse con el condicional múltiple (if-elif-else)
                case 1:
                    print("Inscripto\n")
                case 2:
                    clave_nueva = input("Ingrese nueva clave (debe tener al menos 6 caracteres): ")
                                        
                    while len(clave_nueva) < 6:                                 #Uso de len() para determinar la longitud mínima de la clave
                        print("La clave debe tener al menos 6 caracteres")
                        clave_nueva = input("Ingrese nueva clave: ")
                                        
                    confirmacion_clave = input("Confirme nueva clave: ")
                                        
                    while clave_nueva != confirmacion_clave:                    #Uso de bucle while para 
                        print("Las claves no coinciden.")
                        clave_nueva = input("Ingrese nueva clave: ")
                        confirmacion_clave = input("Confirme nueva clave: ")
                                        
                    #if (len(clave_nueva) >= 6) and clave_nueva == confirmacion_clave:   (antes había hecho este bloque if, luego me di cuenta que no era necesario)
                    print("Clave actualizada con éxito\n")
                    clave_correcta = clave_nueva
                case 3:
                    print("'Estudiar no es tener todas las respuestas, sino animarse a habitar las preguntas. Si dudás, estás aprendiendo; si no sabés, estás exactamente donde empieza el verdadero conocimiento\n'")
                case 4:
                    print("Sesión finalizada")
                    break                               #Uso de break para terminar el bucle while
else:
    print("Cuenta bloqueada")                          #Si todo lo anterior no ocurre, es decir el ciclo for termina sin que las variables coincidan con los datos ingresados, termina el programa