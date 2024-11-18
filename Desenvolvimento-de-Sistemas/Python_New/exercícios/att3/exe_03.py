# 3)ler 3 números Depois de ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

maior_num = num1

if maior_num < num2:
    maior_num = num2

if maior_num < num3:
    maior_num = num3

print(f"O maior número é {maior_num}")

num = int(input("Digite um número:"))
maior_num = num

while num != -1:

    num = int(input("Digite um número:"))
    
    if maior_num < num:
        maior_num = num

print(f'O maior número é {maior_num}')