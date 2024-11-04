# pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
# se for par, avalie um novo c0 como c0 ÷ 2;
# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# se c0 ≠ 1 , volte ao ponto 2.

num = int(input("Digite um número: "))
cont = 0

while num != 1:
    if num % 2 == 0:
        num /= 2
        print(num)
    else:
        num = 3 * num + 1
        print(num)
    cont += 1

print(f"ocorreram {cont} vezes")

