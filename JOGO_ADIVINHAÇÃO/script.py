import random

aleatorio = random.randint(1,10)
chances = 0

while True:
    palpite = int(input("Adivinhe qual o número de 1 a 10: "))
    chances += 1

    if palpite == aleatorio:
        print("Parabéns! Acertou em",chances,"tentativas!")
        break
    elif palpite < aleatorio:
        print("Número baixo! Tente novamente.")
    else:
        print("Número alto! Tente novamente.")