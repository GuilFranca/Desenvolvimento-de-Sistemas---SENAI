# 2).Maior e Menor
# a)  Crie um programa que solicite ao usuário que insira 4 números.
# b)  Identifique e imprima o maior e o menor número da lista inserida.


num = int(input("Digite um número: "))
maior_num = num

for i in range(3):
    num = int(input("Digite um número: "))
    
    if maior_num < num:
        maior_num = num

print(f"O maior número é {maior_num}")
