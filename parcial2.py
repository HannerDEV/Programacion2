# ==========================================================
# ESTRUCTURA BASE
# ==========================================================

option = 0

print("Programación de Computadores II 2026-2")

CATALOGO_EQUIPOS = [
    {"id": 101, "nombre": "Osciloscopio Digital",
     "categoria": "Medición", "disponible": True},
    {"id": 102, "nombre": "Multímetro Fluke",
     "categoria": "Medición", "disponible": True},
    {"id": 103, "nombre": "Fuente de Poder DC",
     "categoria": "Energía", "disponible": False},
    {"id": 104, "nombre": "Generador de Señales",
     "categoria": "Medición", "disponible": True},
    {"id": 105, "nombre": "Kit Arduino Mega",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 106, "nombre": "Cautín de Estación",
     "categoria": "Herramientas", "disponible": True},
    {"id": 107, "nombre": "Protoboard Grande",
     "categoria": "Herramientas", "disponible": True},
    {"id": 108, "nombre": "Pinzas Antiestáticas",
     "categoria": "Herramientas", "disponible": False},
    {"id": 109, "nombre": "Multímetro Digital Bás.",
     "categoria": "Medición", "disponible": True},
    {"id": 110, "nombre": "Sensor ultrasónico HC-SR04",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 111, "nombre": "Raspberry Pi 4 Model B",
     "categoria": "Microcontroladores", "disponible": False},
    {"id": 112, "nombre": "Tarjeta ESP32 Wi-Fi/BT",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 113, "nombre": "Amplificador Operacional IC",
     "categoria": "Componentes", "disponible": True},
    {"id": 114, "nombre": "Kit de Resistencias Varias",
     "categoria": "Componentes", "disponible": True},
    {"id": 115, "nombre": "Condensadores Cerámicos",
     "categoria": "Componentes", "disponible": True},
    {"id": 116, "nombre": "Transistores NPN/PNP",
     "categoria": "Componentes", "disponible": True},
    {"id": 117, "nombre": "Diodos LED Variados",
     "categoria": "Componentes", "disponible": True},
    {"id": 118, "nombre": "Protoboard Mediana",
     "categoria": "Herramientas", "disponible": False},
    {"id": 119, "nombre": "Alicates de Corte",
     "categoria": "Herramientas", "disponible": True},
    {"id": 120, "nombre": "Destornillador de Precisión",
     "categoria": "Herramientas", "disponible": True},
    {"id": 121, "nombre": "Analizador Lógico USB",
     "categoria": "Medición", "disponible": True},
    {"id": 122, "nombre": "Multímetro de Gancho",
     "categoria": "Medición", "disponible": False},
    {"id": 123, "nombre": "Cargador de Pilas Recargables",
     "categoria": "Energía", "disponible": True},
    {"id": 124, "nombre": "Batería de Litio 3.7V",
     "categoria": "Energía", "disponible": True},
    {"id": 125, "nombre": "Módulo Relevador 4 Canales",
     "categoria": "Componentes", "disponible": True},
    {"id": 126, "nombre": "Sensor de Temperatura DHT11",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 127, "nombre": "Sensor de Gas MQ-2",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 128, "nombre": "Motor a Pasos NEMA 17",
     "categoria": "Actuadores", "disponible": True},
    {"id": 129, "nombre": "Servomotor SG90",
     "categoria": "Actuadores", "disponible": True},
    {"id": 130, "nombre": "Motor DC con Reductora",
     "categoria": "Actuadores", "disponible": False},
    {"id": 131, "nombre": "Driver L298N para Motores",
     "categoria": "Componentes", "disponible": True},
    {"id": 132, "nombre": "Pantalla LCD 16x2 I2C",
     "categoria": "Componentes", "disponible": True},
    {"id": 133, "nombre": "Matriz LED 8x8",
     "categoria": "Componentes", "disponible": True},
    {"id": 134, "nombre": "Teclado Matricial 4x4",
     "categoria": "Componentes", "disponible": True},
    {"id": 135, "nombre": "Módulo Bluetooth HC-05",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 136, "nombre": "Módulo Wi-Fi ESP8266",
     "categoria": "Microcontroladores", "disponible": True},
    {"id": 137, "nombre": "Cable UTP Categoria 6 (m)",
     "categoria": "Redes", "disponible": True},
    {"id": 138, "nombre": "Crimpeadora RJ45",
     "categoria": "Herramientas", "disponible": True},
    {"id": 139, "nombre": "Probador de Cables de Red",
     "categoria": "Medición", "disponible": True},
    {"id": 140, "nombre": "Switch de Red 8 Puertos",
     "categoria": "Redes", "disponible": False},
    {"id": 141, "nombre": "Router Inalámbrico Lab",
     "categoria": "Redes", "disponible": True},
    {"id": 142, "nombre": "Estación de Soldar Aire Caliente",
     "categoria": "Herramientas", "disponible": True},
    {"id": 143, "nombre": "Estaño para Soldadura (rollo)",
     "categoria": "Herramientas", "disponible": True},
    {"id": 144, "nombre": "Flux en Pasta",
     "categoria": "Herramientas", "disponible": True},
    {"id": 145, "nombre": "Lupa con Brazo de Sujeción",
     "categoria": "Herramientas", "disponible": True},
    {"id": 146, "nombre": "Generador de Funciones DDS",
     "categoria": "Medición", "disponible": False},
    {"id": 147, "nombre": "Puntas de Prueba para Osciloscopio",
     "categoria": "Medición", "disponible": True},
    {"id": 148, "nombre": "Transformador AC/AC",
     "categoria": "Energía", "disponible": True},
    {"id": 149, "nombre": "Panel Solar Pequeño 5V",
     "categoria": "Energía", "disponible": True},
    {"id": 150, "nombre": "Inversor de Corriente DC/AC",
     "categoria": "Energía", "disponible": True}
]

USUARIOS = [
    "Ana Pérez", "Carlos Gómez", "María Rodríguez", "Juan Martínez",
    "Luisa Fernández", "Andrés López", "Sofía Torres", "David Ramírez",
    "Valentina Díaz", "Mateo Morales", "Camila Rojas", "Santiago Castro",
    "Lucía Vargas", "Daniel Ortiz", "Paula Jiménez", "Gabriel Silva",
    "Elena Mendoza", "Alejandro Ruiz", "Valeria Herrera", "Felipe Medina"
]

MATRIZ_LABORATORIO = [
    [1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1]
]


# ==========================================================
# 1. GESTIÓN DEL CATÁLOGO
# ==========================================================

def agregar_equipo():
    try:
        id_equipo = int(input("Ingrese el ID: "))

        for equipo in CATALOGO_EQUIPOS:
            if equipo["id"] == id_equipo:
                print("Ya existe un equipo con ese ID.")
                return

        nombre = input("Ingrese el nombre: ")
        categoria = input("Ingrese la categoría: ")

        disponible = input(
            "¿Está disponible? (1=Sí, 0=No): "
        )

        if disponible not in ("0", "1"):
            print("Valor de disponibilidad inválido.")
            return

        nuevo_equipo = {
            "id": id_equipo,
            "nombre": nombre,
            "categoria": categoria,
            "disponible": disponible == "1"
        }

        CATALOGO_EQUIPOS.append(nuevo_equipo)

        print("Equipo agregado correctamente.")

    except ValueError:
        print("El ID debe ser un número entero.")


def editar_equipo():
    try:
        id_buscar = int(input("Ingrese el ID del equipo: "))

        for equipo in CATALOGO_EQUIPOS:
            if equipo["id"] == id_buscar:

                print("\nEquipo encontrado.")

                nombre = input(
                    f"Nuevo nombre [{equipo['nombre']}]: "
                )

                categoria = input(
                    f"Nueva categoría [{equipo['categoria']}]: "
                )

                disponibilidad = input(
                    "¿Disponible? (1=Sí, 0=No): "
                )

                if nombre:
                    equipo["nombre"] = nombre

                if categoria:
                    equipo["categoria"] = categoria

                if disponibilidad == "1":
                    equipo["disponible"] = True
                elif disponibilidad == "0":
                    equipo["disponible"] = False

                print("Equipo actualizado.")
                return

        print("No se encontró el equipo.")

    except ValueError:
        print("El ID debe ser un número entero.")


def mostrar_equipos():
    print("\n========== CATÁLOGO ==========")

    for equipo in CATALOGO_EQUIPOS:

        estado = "Disponible" if equipo["disponible"] else "No disponible"

        print(
            f"ID: {equipo['id']} | "
            f"Nombre: {equipo['nombre']} | "
            f"Categoría: {equipo['categoria']} | "
            f"Estado: {estado}"
        )


def eliminar_equipo():
    try:
        id_eliminar = int(input("Ingrese el ID a eliminar: "))

        for posicion, equipo in enumerate(CATALOGO_EQUIPOS):

            if equipo["id"] == id_eliminar:
                CATALOGO_EQUIPOS.pop(posicion)

                print("Equipo eliminado correctamente.")
                return

        print("No se encontró el equipo.")

    except ValueError:
        print("El ID debe ser un número entero.")


def menu_equipos():
    while True:

        print("\n===== GESTIÓN DE EQUIPOS =====")
        print("1. Agregar")
        print("2. Editar")
        print("3. Mostrar")
        print("4. Eliminar")
        print("5. Regresar")

        try:
            opcion = int(input("Seleccione: "))

            if opcion == 1:
                agregar_equipo()

            elif opcion == 2:
                editar_equipo()

            elif opcion == 3:
                mostrar_equipos()

            elif opcion == 4:
                eliminar_equipo()

            elif opcion == 5:
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número.")


# ==========================================================
# 2. FILTRADO INTELIGENTE
# ==========================================================

def filtrar_inventario():

    categoria = input("Ingrese la categoría: ")

    try:
        n = int(input("Ingrese N: "))

        if n < 0:
            print("N no puede ser negativo.")
            return

        # LIST COMPREHENSION
        # .copy() crea copias seguras de los diccionarios
        filtrados = [
            equipo.copy()
            for equipo in CATALOGO_EQUIPOS
            if equipo["categoria"].lower() == categoria.lower()
            and equipo["disponible"] is True
        ]

        # SLICING
        resultado = filtrados[:n]

        print("\n===== RESULTADO =====")

        for equipo in resultado:
            print(
                f"{equipo['id']} - "
                f"{equipo['nombre']}"
            )

        print(f"\nSe muestran {len(resultado)} equipos.")

    except ValueError:
        print("N debe ser un número entero.")


# ==========================================================
# 3. ASIGNACIÓN MASIVA
# ==========================================================

def asignar_prestamos():

    try:
        k = int(input("Ingrese la cantidad K: "))

        if k <= 0:
            print("K debe ser mayor que cero.")
            return

        # SLICING: primeros K usuarios
        usuarios_k = USUARIOS[:k]

        # LIST COMPREHENSION:
        # obtener únicamente equipos disponibles
        disponibles = [
            equipo
            for equipo in CATALOGO_EQUIPOS
            if equipo["disponible"] is True
        ]

        # SLICING: primeros K equipos disponibles
        equipos_k = disponibles[:k]

        if len(usuarios_k) < k:
            print("No existen suficientes usuarios.")
            return

        if len(equipos_k) < k:
            print("No existen suficientes equipos disponibles.")
            return

        print("\n===== ASIGNACIONES =====")

        # ZIP para emparejar usuarios y equipos
        asignaciones = zip(usuarios_k, equipos_k)

        # ENUMERATE para numerar
        for numero, (usuario, equipo) in enumerate(
            asignaciones,
            start=1
        ):

            # TUPLA
            asignacion = (
                usuario,
                equipo["id"],
                equipo["nombre"]
            )

            print(
                f"{numero}. Usuario: {asignacion[0]} | "
                f"Equipo: {asignacion[1]} - "
                f"{asignacion[2]}"
            )

            # El equipo deja de estar disponible
            equipo["disponible"] = False

    except ValueError:
        print("K debe ser un número entero.")


# ==========================================================
# 4. MATRIZ DE LABORATORIOS
# ==========================================================

def mostrar_matriz():

    print("\n===== MATRIZ DE LABORATORIOS =====")
    print("0 = Desocupado | 1 = Ocupado\n")

    for numero, fila in enumerate(
        MATRIZ_LABORATORIO,
        start=1
    ):
        print(f"Laboratorio {numero}: ", end="")

        for valor in fila:
            print(valor, end=" ")

        print()


def actualizar_matriz():

    try:
        laboratorio = int(
            input("Ingrese laboratorio (1-3): ")
        )

        bloque = int(
            input("Ingrese bloque (1-5): ")
        )

        estado = int(
            input("Ingrese estado (0=Libre, 1=Ocupado): ")
        )

        # Convertimos a índices de Python
        fila = laboratorio - 1
        columna = bloque - 1

        if estado not in (0, 1):
            print("El estado debe ser 0 o 1.")
            return

        # Acceso a matriz bidimensional
        MATRIZ_LABORATORIO[fila][columna] = estado

        print("Matriz actualizada correctamente.")

    except IndexError:
        print("Error: laboratorio o bloque fuera de rango.")

    except ValueError:
        print("Error: debe ingresar números enteros.")


def menu_matriz():

    while True:

        print("\n===== MATRIZ HORARIA =====")
        print("1. Mostrar matriz")
        print("2. Actualizar bloque")
        print("3. Regresar")

        try:
            opcion = int(input("Seleccione: "))

            if opcion == 1:
                mostrar_matriz()

            elif opcion == 2:
                actualizar_matriz()

            elif opcion == 3:
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número.")


# ==========================================================
# 5. MENÚ PRINCIPAL
# ==========================================================

def main():

    while True:

        print("\n======================================")
        print(" SISTEMA DE LABORATORIOS")
        print("======================================")
        print("1. Gestionar catálogo de equipos")
        print("2. Filtrado inteligente de inventario")
        print("3. Asignación masiva de préstamos")
        print("4. Consultar / actualizar matriz")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                menu_equipos()

            elif opcion == 2:
                filtrar_inventario()

            elif opcion == 3:
                asignar_prestamos()

            elif opcion == 4:
                menu_matriz()

            elif opcion == 5:
                print("Programa finalizado.")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número entero.")


# ==========================================================
# EJECUCIÓN
# ==========================================================

main()