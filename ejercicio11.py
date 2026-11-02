import random

scores: tuple[int, ...] = (400, 200, 150, 100, 50, 40, 20, 0)

weight_scores: tuple[int, ...] = (1, 2, 4, 6, 9, 10, 20, 35)

def get_score() -> int:
    return random.choices(scores, weights= weight_scores, k=1)[0]

def initial_menu() -> tuple[list[int], float]:
    while True:
        try:
            players_num = int(input("Seleccione el numero de jugadores, maximo 12: "))
            if players_num > 12 or players_num < 1:
                print("numero de jugadores invalido")
                continue

            max_score = int(input("Ingrese el puntaje maximo para ganar en multiplos de 1.000, maximo 10.000: "))
            if max_score > 10000 or max_score % 1000 != 0 or max_score <= 0:
                print("Puntaje maximo invalido")
                continue
            break
        except ValueError:
            print("Valor ingresado invalido")

    score_players = [0]*players_num

    return score_players, max_score

def play(score_players, max_score):
    while True:
        for i, _ in enumerate(score_players):
            print(f"Turno del jugador {i + 1}")
            print(f"Puntaje actual: {score_players[i]}")
            acumulated_score = 0

            for j in range(1, 4):
                input(f"Presione enter para lanzar la bola, intento{j}: ")
                new_score = get_score()
                print(f"Puntaje conseguido {new_score}")
                score_players[i] += new_score
                acumulated_score += new_score

                if score_players[i] >= max_score:
                    print(f"Ha ganado el jugador {i + 1}")
                    return
                
            if acumulated_score == 0:
                print("Ha perdido 50 puntos")
                score_players[i] -= 50


def main():
    print("     BIENVENIDO AL JUEGO DE LA RANA      ")
    score_players, max_score = initial_menu()
    play(score_players, max_score)

        

if __name__ == "__main__":
    main()