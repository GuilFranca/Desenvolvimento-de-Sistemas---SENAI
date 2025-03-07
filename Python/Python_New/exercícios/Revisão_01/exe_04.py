# 4)Implemente uma lojinha virtual simples! Onde possamos ter um catálogo com 5 produtos e nesse podemos adicionar ao carrinho ou visualizar-lo. Até chegarmos na finalização do qual mostrará o valor total

produtos = {
    'agua' : 2.00,
    'banana' : 1.00,
    'camarao' : 35.00,
    'doritos' : 20.00,
    'ervilha' : 10.00,
    'frango' : 25.00,
    'guarana' : 7.00,
    'hamburguer' : 15.00
}

carrinho = {}

for chave, valor in produtos.items():
    print(f'{chave} : {valor}')

operacao = 0

while operacao != '4':
    print('\n-=-=-=Lista de afazeres=-=-=-')
    print("Digite 1 para vizualizar")
    print("Digite 2 para adicionar")
    print("Digite 3 para excluir")
    print("Digite 4 para finalizar compra")

    operacao = input()

    match operacao:
        case '1':
            print(carrinho)
        case '2':
            action = input('Digite o produto que será adicionada: ')
            if action in produtos:
                carrinho[action] = produtos[action]
        case '3':
            action = input('Digite qual produto deve ser excluida: ')
            carrinho.pop(action)
        case '4':
            print('Compra Finalizada')
            print(carrinho.items())
            soma = sum(carrinho.values())
            print(f'O valor total é de R${soma}')
        case _:
            print('Valor invalido')