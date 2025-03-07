secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

tentativa = int(input("Digite um número: "))
num_tentativas = 1

while tentativa != secret_number:
    if tentativa < secret_number:
        print("O número secreto é maior")
    elif tentativa > secret_number:
        print("O número secreto é menor")
    num_tentativas += 1
    tentativa = int(input("Digite um número: "))



print("Você acertou!!")
print(f"Número de tentativas: {num_tentativas}")

