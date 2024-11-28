# 1)Peça ao usuário dois números e uma operação matemática (+, -, *, /). Execute a operação e trate erros como divisão por zero e operação inválida.

# num_1 = float(input("Digite o primeiro número: "))
# operacao = input("Digite a operção: ")
# num_2 = float(input("Digite o segundo número: "))

# try:

#     match operacao:
#         case '+':
#             print(f'{num_1} {operacao} {num_2} = {num_1 + num_2}')
#         case '-':
#             print(f'{num_1} {operacao} {num_2} = {num_1 - num_2}')
#         case '*':
#             print(f'{num_1} {operacao} {num_2} = {num_1 * num_2}')
#         case '/':
#             print(f'{num_1} {operacao} {num_2} = {num_1 / num_2}')
#         case _:
#             print('Valor invalido')

# except ZeroDivisionError as erro:
#     print("Não pode dividir por zero")
#     print(erro)

def calculadora():
    try:
        # Solicita os números e a operação ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        # Dicionário de operações usando lambda
        operacoes = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
        }

        # Verifica se a operação é válida e executa
        if operacao in operacoes:
            resultado = operacoes[operacao](num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Erro: Operação inválida.")
    except ValueError:
        print("Erro: Entrada inválida. Digite números válidos.")

# Chama a função
calculadora()
