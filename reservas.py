import random

#Diccionarios
ciudades = {
        1: "Medellín",
        2: "Bogotá",
        3: "Cartagena"
    }

dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo"
    }

meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

generos = {
    1: "Señor",
    2: "Señora"
}

preferencias = {
    1: "A",
    2: "C",
    3: "B"
}

while True:
    try:
        genero = int(input("Elija una opcion con la que se identifique,(1: Señor, 2: Señora): "))
        if genero in generos:
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")

print(f"{generos[genero]} {nombre} {apellido}, ¡Bienvenido a Monar Airlines!")

while True:
    try:
        origen = int(input("Ingresa el número de tu ciudad de origen (1: Medellín, 2: Bogotá, 3: Cartagena): "))
        if origen in ciudades:
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")

while True:
    try:
        destino = int(input("Ingresa el número de tu ciudad destino (1: Medellín, 2: Bogotá, 3: Cartagena): "))
        if destino in ciudades and destino != origen:
            break
        elif destino == origen:
            print("El destino no puede ser igual al origen. Intenta de nuevo.")
        else:
            print("Opción incorrecta. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")

while True:
    try:
        dia_semana = int(input("Ingrese el número del día de la semana (1: lunes, 2: martes, etc.): "))
        if dia_semana in dias:
            break
        else:
            print("Número incorrecto. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")

while True:
    try:
        dia_mes = int(input("Introduzca el día del mes (1-30): "))
        if 1 <= dia_mes <= 30:
            break
        else:
            print("Día inválido. Intente de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")

while True:
    try:
        mes = int(input("Ingresa el número del mes de tu viaje (1: enero, 2: febrero, etc.): "))
        if mes in meses:
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")

while True:
    try:
        pref = int(input("Prefiere usted 1: ventana, 2: pasillo, 3: cualquiera : "))
        if pref in preferencias:
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un valor válido.")

if origen == 1 and destino == 2:
    distancia = 240
elif origen == 1 and destino == 3:
    distancia = 461
elif origen == 2 and destino == 1:
    distancia = 240
elif origen == 2 and destino == 3:
    distancia = 657
elif origen == 3 and destino == 1:
    distancia = 657
else:
    distancia = 461

if distancia < 400 and dia_semana <= 4:
    precio = 79900
if distancia < 400 and dia_semana >= 5:
    precio = 119900
if distancia >= 400 and dia_semana <= 4:
    precio =156900
if distancia >=400 and dia_semana <= 5:
    precio = 213000

num_asiento = random.randint(1, 29)
asiento = num_asiento, {preferencias[pref]}

print(f"Tu vuelo de {ciudades[origen]} a {ciudades[destino]} del {dias[dia_semana]} {dia_mes} de {meses[mes]} esta reservado.")
print(f"Precio del boleto: {precio}")
print(f"Tu asiento es: {asiento}")