# 1) faça uma calculadora com as 4 operações configuradas ( +,-,*,/)

# num1 = float(input("Digite o primeiro número: "))
# operador = input("Digite o operador: ")
# num2 = float(input("Digite o segundo número: "))

# match operador:
#     case '+':
#         print(f'{num1} {operador} {num2} = {num1 + num2}')
#     case '-':
#         print(f'{num1} {operador} {num2} = {num1 - num2}')
#     case '*':
#         print(f'{num1} {operador} {num2} = {num1 * num2}')
#     case '/':
#         print(f'{num1} {operador} {num2} = {num1 / num2}')
#     case _: #captura valores não esperados
#         print(f'Algum valor enviado incorretamente')

def calculadora():
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    operation = input("Digite a operação (+, -, *, /): ")

    operações = {
        '+' : num_1 + num_2,
        '-' : num_1 - num_2,
        '*' : num_1 * num_2,
        '/' : num_1 / num_2
    }

    print(f'{num_1} {operation} {num_2} = {operações[operation]}')

calculadora()