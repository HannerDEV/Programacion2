from typing import Dict, TypedDict

class Subject(TypedDict):
    note: float
    credits: int

Nota = Dict[str, Subject]

notes: Nota = {}

def pedir_notas() -> None:
    name = input("Ingrese el nombre de la materia: ").casefold().strip()
    while True:
        try:
            note = float(input("Ingrese la nota de la materia: "))
            if not (note >= 0 and note <= 50):
                print("La nota debe estar entre 0 y 50")
                continue
            credits = int(input("Ingrese los creditos de la materia"))
            if not(credits > 0 and credits <= 6):
                print("Los creditos deben estar entre 0 y 6")
                continue
            break
        except ValueError:
            print("Valor ingresado invalido")
        

    notes[name] = {
        "note": note,
        "credits": credits
    }

def calculate_weighted_mean() -> None:
    if not notes:
        print("no hay materia registradas")
        return

    weighted_mean = 0.0
    credits = 0

    for nota in notes.values():
        weighted_mean += nota["note"]*nota["credits"]
        credits += nota["credits"]

    weighted_mean /= credits

    print(weighted_mean)

def calculate_aritmetic_mean() -> None:
    if not notes:
        print("no hay materia registradas")
        return
    aritmetic_mean = 0.0
    i = 0

    for nota in notes.values():
        aritmetic_mean += nota["note"]
        i += 1

    aritmetic_mean /= i

    print(aritmetic_mean)




def main() -> None:
    options = {"1": pedir_notas, "2": calculate_weighted_mean, "3": calculate_aritmetic_mean}    
    print(f"{'='*8}BIENVENIDO AL SISTEMA DE NOTAS{'='*8}")
    while True:
        op = input("1. Ingresar nueva materia  2. Calcular ponderado 3. Calcular promedio aritmetico   4. Salir\n")
        if op == "4":
            break
        if op in options:
            options[op]()
    

if __name__ == "__main__":
    main()