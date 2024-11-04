# Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário. 

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.

# Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual

hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

position = int(input("Digite qual posição da lista deseja editar: "))
num = int(input("Digite o número que você quer colocar no lugar: "))

hat_list [position] = num
print(hat_list)
print(hat_list[position])


