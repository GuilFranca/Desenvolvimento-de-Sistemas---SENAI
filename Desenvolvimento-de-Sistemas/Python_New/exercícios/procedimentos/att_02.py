# 2) Crie uma função fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.

# def paridade(num):
#     if num % 2 != 0:
#         print(f"O número {num} é impar")
#     else:
#         print(f"O número {num} é par")

# num = int(input("Digite um número: "))
# paridade(num)

def parImpar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

print(parImpar(4))