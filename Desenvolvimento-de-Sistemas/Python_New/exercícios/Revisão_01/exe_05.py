# 5)aplicação que pegue o número de clientes em uma mesa, o valor total da conta e após isso divida a conta de forma igual a todos os clientes

clientes = int(input('Digite o número de clientes: '))
valores = {}

for i in range(clientes):
    nome = input('Nome do cliente: ')
    conta = float(input(f'Digite o valor da conta do {nome}: '))
    valores.setdefault(nome, conta)

total = sum(valores.values())
dividido = total / clientes

print(f'O valor total foi de R${total}')
print(f'O valor dividido para cada um foi de R${dividido}')

