# 3)Crie um jogo simples em Python:Um número secreto entre 1 e 100 é gerado aleatoriamente.O jogador tem 5 tentativas para adivinhar o número.Após cada tentativa, o programa deve informar:
# "Muito alto!" se o palpite for maior que o número.
# "Muito baixo!" se o palpite for menor que o número.
# "Parabéns, você acertou!" se o palpite for igual ao número.
# Caso o jogador não acerte após 5 tentativas, exiba "Game Over! O número era X".
# Utilize a biblioteca random para gerar o número secreto.

import random

chute = -1
numero_chute = 0
numero_aleatorio = int(random.random() * 100 + 1)
print(numero_aleatorio)
print('-=-=NÚMERO SECRETO=-=-')

while (chute != numero_aleatorio) and (numero_chute < 5):
    print(f'Número de vidas: {5 - numero_chute}')
    chute = int(input('Adivinhe o número: '))
    if chute == numero_aleatorio:
        print(f'Você acertou! O número secreto era {numero_aleatorio}')
        break
    elif chute > numero_aleatorio:
        print(f'O número secreto é menor que {chute}.')
    elif chute < numero_aleatorio:
        print(f'O número secreto é maior que {chute}.')
    numero_chute += 1

if numero_chute >= 5:
    print(f'GAME OVER! O número secreto era {numero_aleatorio}')
