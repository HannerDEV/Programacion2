def main() -> None:
    months = (
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        )

    max_length = 12
    min_length = 1
    executing = True
    while executing:
        try:
            num = int(input("Digite el numero del mes que quiere imprimir el pantalla (0. para salir): "))
            if num == 0:
                print("Cerrando el programa...")
                executing = False
            elif num >= min_length and num <= max_length:
                posicion = num - 1
                print(f"El mes solicitado es: {months[posicion]}")
            else:
                print("Mes no existente")
        except ValueError:
            print("Error de entrada")



if __name__ == "__main__":
        main()