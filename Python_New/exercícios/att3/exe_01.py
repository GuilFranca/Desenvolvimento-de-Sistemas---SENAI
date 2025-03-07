# 1) Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).

num = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{num} X {i} = {num * i}")