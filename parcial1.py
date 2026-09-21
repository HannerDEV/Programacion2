TARIFA_ESTUDIANTE = 5000
TARIFA_DOCENTE = 12000
TARIFA_EXTERNO = 20000
TARIFA_INFANTE = 3000


def registrar_visitante():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    print("\nTipo de visitante:")
    print("1. Estudiante")
    print("2. Docente")
    print("3. Externo")
    print("4. Infante")

    tipo = int(input("Seleccione el tipo: "))

    while tipo < 1 or tipo > 4:
        print("Tipo inválido.")
        tipo = int(input("Seleccione el tipo: "))

    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }

    print("\nDía de la semana:")
    for numero, dia in dias.items():
        print(f"{numero}. {dia}")

    dia = int(input("Seleccione el día: "))

    while dia < 1 or dia > 7:
        print("Día inválido.")
        dia = int(input("Seleccione el día: "))

    visitante = {
        "nombre": nombre,
        "edad": edad,
        "tipo": tipo,
        "dia": dias[dia]
    }

    return visitante


def calcular_tarifa(visitante):
    edad = visitante["edad"]
    tipo = visitante["tipo"]

    tarifas = {
        1: TARIFA_ESTUDIANTE,
        2: TARIFA_DOCENTE,
        3: TARIFA_EXTERNO,
        4: TARIFA_INFANTE
    }

    tarifa = tarifas[tipo]

    # Infante menor de 5 años no paga
    if tipo == 4 and edad < 5:
        return 0

    # Mayores de 60 años pagan el 50%
    if edad > 60:
        return tarifa * 0.50

    return tarifa


def generar_reporte(historial):
    nombres_tipos = {
        1: "Estudiante",
        2: "Docente",
        3: "Externo",
        4: "Infante"
    }

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    cantidad_tipo = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    cantidad_dia = {
        dia: 0 for dia in dias
    }

    dinero_tipo = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    total = 0

    for visitante in historial:
        tipo = visitante["tipo"]
        dia = visitante["dia"]
        tarifa = visitante["tarifa"]

        cantidad_tipo[tipo] += 1
        cantidad_dia[dia] += 1
        dinero_tipo[tipo] += tarifa
        total += tarifa

    print("\n========== REPORTE GENERAL ==========")

    print("\nCantidad de visitantes según tipo:")
    for tipo in range(1, 5):
        print(
            f"{nombres_tipos[tipo]}: "
            f"{cantidad_tipo[tipo]}"
        )

    print("\nCantidad de visitantes por día:")
    for dia in dias:
        print(f"{dia}: {cantidad_dia[dia]}")

    print("\nRecaudación por tipo:")
    for tipo in range(1, 5):
        print(
            f"{nombres_tipos[tipo]}: "
            f"${dinero_tipo[tipo]:,.0f}"
        )

    print(f"\nTOTAL DE RECAUDACIÓN: ${total:,.0f}")


def main():
    historial = []

    while True:
        print("\n========== PARQUE ECOLÓGICO ==========")
        print("1. Registrar visitante")
        print("2. Calcular tarifa")
        print("3. Generar reporte")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            visitante = registrar_visitante()

            tarifa = calcular_tarifa(visitante)
            visitante["tarifa"] = tarifa

            historial.append(visitante)

            print("\nVisitante registrado correctamente.")
            print(f"Valor a pagar: ${tarifa:,.0f}")

        elif opcion == 2:
            if len(historial) == 0:
                print("\nNo hay visitantes registrados.")
            else:
                ultimo = historial[-1]
                tarifa = calcular_tarifa(ultimo)

                print(
                    f"\nTarifa de {ultimo['nombre']}: "
                    f"${tarifa:,.0f}"
                )

        elif opcion == 3:
            if len(historial) == 0:
                print("\nNo hay información para generar el reporte.")
            else:
                generar_reporte(historial)

        elif opcion == 4:
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida.")


main()