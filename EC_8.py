#8.	Realice un programa que permita realizar un bingo digital
import random

bingo1 = 0
bingo2 = 0

# Suponiendo que 'bingo_1' y 'bingo_2' son listas con los números ganadores de cada juego
bingo_1 = [1, 2, 3]
bingo_2 = [4, 5, 6]

while bingo1 != "BINGO1" and bingo2 != "BINGO2":  # El bucle debe continuar hasta que uno de los jugadores gane

    contador = 0
    s = []

    while contador < 3:  # Generar una lista de tres números aleatorios para cada juego
        numero_aleatorio = random.randint(1, 10)
        s.append(numero_aleatorio)
        contador += 1

    print("Números generados para bingo1:", s)

    # Comprobar si bingo1 gana
    if s == bingo_1:
        print("¡El ganador es el bingo1!")
        bingo1 = "BINGO1"

    print("Números generados para bingo2:", s)

    # Comprobar si bingo2 gana
    if s == bingo_2:
        print("¡El ganador es el bingo2!")
        bingo2="BINGO2"