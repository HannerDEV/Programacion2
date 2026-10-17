def show_database(database: tuple) -> None:
    for i in range(len(database)):
        user = database[i]
        name = user[0]
        last_name = user[1]
        document_id = user[2]
        address = user[3]
        number = user[4]

        print(f"\n{name:<20} | {last_name:<20} | {document_id:<20} | {address:<20} | {number:<20}")
        print()

def edit_data(database: tuple) -> None:
    opciones = ("nombres", "apellidos", "documento", "direccion", "numero de telefono")
    
    name = input("digite el nombre del usuario")

    found = False

    for user in database:

        if name.lower() == user[0].lower():
            found = True
            print(f"editar datos de {user[0]} {user[1]} ")
            try:
                print("""
                1.editar nombres
                2.editar apelllidos
                3.editar documento
                4.editar direccion
                5.editar numero de telefono
                """)
                eleccion_num = int(input("Digite la eleccion que requiere: ")) - 1

                if 0<=eleccion_num < len(opciones):
                    eleccion = opciones[eleccion_num]
                    new_value = input(f"Digite el nuevo valor del campo {eleccion}: ")
                    user[eleccion_num] = new_value
                    print("campo actualizado")
                else:
                    print("opcion fuera de rango")
            except ValueError:
                print("Error de valor ingresado")

    if not found:
        print("Usuario no encontrado")

def main() -> None:

    base_datos = (
            [
                "Carlos Andrés",
                "Gómez Pérez",
                "1012345678",
                "Calle 45 # 12-34",
                "3001234567",
            ],
            [
                "María Fernanda",
                "Rojas Silva",
                "1098765432",
                "Carrera 15 # 88-10",
                "3159876543",
            ],
            [
                "Luis Eduardo",
                "Martínez Torres",
                "1033445566",
                "Avenida 68 # 45-20",
                "3104445566",
            ]
        )
    opciones = {
                    1: show_database,
                    2: edit_data
                }

    executing = True

    while executing:
        try:

            print("1. imprimir base de datos 2. editar datos de usuario 0. Salir")
            num = int(input("Digite la opcion que deseas elegir: "))
            eleccion = opciones.get(num)

            if num == 0:
                print("Cerrando el sistema...")
                executing = False
            elif eleccion:
                eleccion(base_datos)
            else:
                print("Opcion invalida")
        except ValueError:
            print("Error de entrada")

if __name__ == "__main__":
    main()
