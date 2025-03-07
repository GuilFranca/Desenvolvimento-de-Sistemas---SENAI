# 2)Escreva um programa para um sistema de controle de estoque de uma loja. O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes dos produtos e os valores são as quantidades disponíveis.Permitir que o usuário escolha uma das opções:
# Adicionar um novo produto ao estoque.
# Atualizar a quantidade de um produto existente.
# Verificar se um produto está disponível (quantidade maior que 0).
# Continuar exibindo o menu até que o usuário escolha sair.

estoque = {}

operador = 0

while operador != 5:
    print('-=-=Estoque=-=-')
    print('1 - ADICIONAR')
    print('2 - ATUALIZAR')
    print('3 - REMOVER')
    print('4 - VISUALIZAR')
    print('5 - SAIR')
    operador = int(input())

    match operador:
        # Adiciona
        case 1:
            # Limpa o terminal
            print("\033c", end="")
            nome = input('Digite o nome do produto: ')
            if nome in estoque:
                print(f'Produto {nome} já cadastrado no estoque.')
            else:
                qtd = int(input('Digite a quantidade: '))
                # Adiciona ao dicionário caso não exista a chave.
                estoque.setdefault(nome,qtd)
            print(estoque)
        # Atualiza
        case 2:
            print("\033c", end="")
            nome = input('Digite o nome do produto: ')
            if nome in estoque:
                qtd = input('Digite a quantidade: ')
                # Atualiza um valor presente no dicionário
                estoque.update({
                    nome : qtd
                })
                print(estoque)
            else:
                print(f'Produto {nome} não encontrado no estoque.')
        # Remove
        case 3:
            print("\033c", end="")
            nome = input('Digite o nome do produto que deseja remover: ')
            estoque.pop(nome)
            print(estoque)
        # Visualizar
        case 4:
            print("\033c", end="")
            print(estoque)
        
        case 5:
            print("\033c", end="")
            print('PROGRAMA ENCERRADO!')