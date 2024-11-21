# 1) Crie uma função que multiplica todos os argumentos não nomeados recebidos e Retorne o total para uma variável e mostre o valor da variável.

def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total

result = mult(2, 3, 4)
print(f"O resultado da multiplicação é: {result}")