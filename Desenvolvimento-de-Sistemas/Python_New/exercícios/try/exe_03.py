# 3)Solicite ao usuário que insira seu peso e altura. Calcule o IMC, mas trate possíveis erros, como entradas inválidas ou divisões por zero. Garanta que o programa sempre informe o status do processo no finall

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em M: '))

try:
    imc = peso / (altura * altura)
    print(imc)
except ZeroDivisionError as erro:
    print('Erro de divisão por ZERO')
    print(erro)
except ValueError as erro:
    print('Erro de valor inserido')
    print(erro)
finally:
    print('Programa executado')