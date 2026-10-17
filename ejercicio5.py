from typing import List

def search(nombres: List[str], nombre: str) -> bool:
    target = nombre.lower()
    return any(x.lower() == target for x in nombres)

def main() -> None:
    nombres: List[str] = [
    "Alejandro",
    "Sofía",
    "Mateo",
    "Valentina",
    "Gabriel",
    "Elena",
    "Ian",
    "Mia",
    "Enzo",
    "Zoe",
    "Leo",
    "Alma",
    "Bruno",
    "Marina",
    "Aurora",
    "Silas",
    "Maya",
    "Oliver",
    "Emma",
    "Liam",
    ]

    while True:
        nombre = input("Escriba el nombre que desea buscar, escriba 0 para salir: ").strip()

        if nombre == "0":
            print("Saliendo del programa...")
            break

        encontrado: bool = search(nombres, nombre)
        if encontrado:
            print("Nombre encontrado en la lista")
        else:
            print("Nombre no encontrado")

if __name__ == "__main__":
    main()