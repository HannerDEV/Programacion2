def show_database(database: tuple) -> None:
    for i in range(len(database)):
        user = database[i]
        name = user[0]
        last_name = user[1]
        id = user[2]
        address = user[3]
        number = user[4]

        print(f"""
        {name:<20} |
        {last_name:<20} |
        {id:<20} |
        {address:<20} |
        {number:<20} |
        """)
        

def main() -> None:

    base_datos = (
            (
                "Carlos Andrés",
                "Gómez Pérez",
                "1012345678",
                "Calle 45 # 12-34",
                "3001234567",
            ),
            (
                "María Fernanda",
                "Rojas Silva",
                "1098765432",
                "Carrera 15 # 88-10",
                "3159876543",
            ),
            (
                "Luis Eduardo",
                "Martínez Torres",
                "1033445566",
                "Avenida 68 # 45-20",
                "3104445566",
            )
        )
    show_database(base_datos)

if __name__ == "__main__":
    main()