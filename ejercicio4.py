from typing import List, Tuple

def clasificar_numeros(numbers: List[int]) -> Tuple[List[int], List[int]]:
    sorted_numbers = sorted(numbers)

    pairs = [x for x in sorted_numbers if not(x & 1)]
    odds = [x for x in sorted_numbers if (x & 1)]

    return  pairs, odds

def capturar_datos() -> List[int] :
    numbers: List[int] = []
    getting = True
    i = 1
    while getting:
        try:
            number = int(input(f"Digite el valor #{i} 0.para terminar la lista : "))
        except ValueError:
            print("Valor ingresado invalido, solo numeros enteros")
            continue
        if not number:
            if not len(numbers):
                print("la lista esta vacia, debe ingresar al menos un dato")
                continue
            else:
                break
        
        numbers.append(number)
        i += 1
    return numbers


def main() -> None:
    print(f"{"="*12} BIENVENIDO AL SISTEMA {"="*12}")

    numbers = capturar_datos()
    pairs, odds = clasificar_numeros(numbers)

    print(f"la lista de numeros pares es la siguiente: {pairs}")
    print(f"la lista de numeros impares es la siguiente: {odds}")

if __name__ == "__main__":
    main()
