equa1: list[float] = []
equa2: list[float] = []

def calculate_determinat(x1, x2 , y1, y2) -> float:
    determinat = x1*y2 - x2*y1
    return determinat

def verify_system(a1, b1, a2, b2) ->float:
    determinat = calculate_determinat(a1, b1, a2, b2)
    if determinat == 0:
        print("Sistema de ecuaciones invalido. ")
        return determinat
    return determinat

def calculate_solutions(general_determinant)-> tuple[float, float]:
    a1, b1, c1, a2, b2, c2 = [*equa1, *equa2]
    x_determinant = calculate_determinat(c1, c2, b1, b2)
    y_determinant = calculate_determinat(a1, a2, c1, c2)

    x = x_determinant/general_determinant
    y = y_determinant/general_determinant

    return x, y 

def get_values() -> float:
    while True:
        try:
            a1 = float(input("Ingrese a1: "))
            b1 = float(input("Ingrese b1: "))
            c1 = float(input("Ingrese c1: "))
            a2 = float(input("Ingrese a2: "))
            b2 = float(input("Ingrese b2: "))
            c2 = float(input("Ingrese c2: "))

            determinat = verify_system(a1, b1, a2, b2)
            if not determinat:
                continue
            equa1.extend([a1, b1, c1])
            equa2.extend([a2, b2, c2])
            break
        except ValueError:
            print("Valor ingresado invalido, intente de nuevo.")
    return determinat
        

def main()-> None:
    print(f"{"="*8}WELCOME TO THE 2X2 EQUATIONS CALCULATOR{"="*8}")
    determinant = get_values()
    x, y = calculate_solutions(determinant)
    print(f"La primera solucion es: {x} La segunda solucion es: {y}")

if __name__ == "__main__":
    main()