#Ejercicio 1 — “Caja del Kiosco”

nombre = input("Por favor, ingrese su nombre: ")

#Validación si nombre queda vacío ""
while not nombre:              
    print("Campo obligatorio")
    nombre = input("Por favor, ingrese su nombre: ")

#Validación con while .isalpha
while not nombre.isalpha():     
    print("Ingreso de datos inválidos")
    nombre = input("Por favor, ingrese su nombre: ")

cant_productos = input("Por favor, ingrese la cantidad de productos a comprar: ")

#Validación si cant_productos queda vacío ""
while not cant_productos:
    print("Campo obligatorio")
    cant_productos = input("Por favor, ingrese la cantidad de productos: ")

#Validación con while .isdigit
while not cant_productos.isdigit():    
    print("Ingreso de datos inválidos")
    cant_productos = input("Ingrese la cantidad en números de productos a comprar: ")

#Validación cantidad > 0 (si ingresa 0, volver a pedir).
while int(cant_productos) <= 0:
    cant_productos = input("Por favor, ingrese una cantidad de productos mayor a 0: ")

#Transformar la variable a un entero
cant_productos = int(cant_productos)

#Inicialización en 0 de los acumuladores <total_sin_descuento> y <ahorro>
total_sin_descuento = 0
ahorro = 0

print("\n")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cant_productos}")

#Bucle de iteración egún la cant_productos ingresada por el usuario
for producto in range(1, cant_productos+1):
    precio = input(f"Ingrese el precio del producto {producto}: $")

    #Validación con while .isdigit
    while not (precio.isdigit()):
        input("Error, debe ingresar un precio válido: ")
    
    #Validación precio no puede ser 0 o negativo
    while int(precio) <= 0:
        precio = input("Error, debe ingresar un precio mayor a 0: ")

    #Transformar la variable a un entero
    precio = int(precio)

    #Uso de la función .lower para aceptar tanto mayúsculas como minusculas
    descuento = input("¿Tiene descuento? (S/N): ").lower()

    #Validación si descuento queda vacío ""
    while not descuento:
        descuento = input("Campo obligatorio. Ingrese (S7N)").lower()

    #Validación si descuento es != a S/N/s/
    while descuento not in ("s","n"):
        descuento = input("Error. Ingrese S/N: ").lower()

    #Actualización del acumulador <total_sin_descuento>
    total_sin_descuento += precio

    #Uso del condicional en el caso de que la opción ingresada sea "s"
    if descuento == "s":
        #Se realiza la operación para extraer el valor del descuento y se actualiza el acumulador <ahorro>
        ahorro += precio * 0.10  
    print(f"Producto: {producto} - Precio: ${precio} - Descuento (S/N): {descuento}")

#Proceso para determinar y asignar la variable <total_con_descuento>
total_con_descuento = total_sin_descuento - ahorro

#Proceso para determinar y asignar la variable <promedio>
promedio = total_sin_descuento / cant_productos

#Salida por pantalla con los datos requeridos
print("//////////////////////////////////////////////////////////")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento}")
print(f"Ahorro total: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")
print(f"Gracias por su compra, {nombre}. Esperamos verle pronto!")
print("//////////////////////////////////////////////////////////")