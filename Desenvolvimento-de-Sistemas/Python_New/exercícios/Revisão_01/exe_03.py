# 3)Crie um programa que permita ao usuário adicionar tarefas a uma lista, marcar como concluídas ou remover tarefas

operacao = 0
afazer = {}

while operacao != '5':
    print('-=-=-=Lista de afazeres=-=-=-')
    print("Digite 1 para vizualizar")
    print("Digite 2 para adicionar")
    print("Digite 3 para atualizar")
    print("Digite 4 para excluir")
    print("Digite 5 para sair")

    operacao = input()

    match operacao:
        case '1':
            print(afazer)
        case '2':
            action = input('Digite a tarefa que será adicionada: ')
            afazer.setdefault(action,'Pendente')
        case '3':
            action = input('Digite qual tarefa deseja atualizar: ')
            if afazer[action] == 'Pendente':
                afazer.update({
                    action : 'Finalizada'
                })
            else:
                afazer.update({
                    action : 'Pendente'
                })
        case '4':
            action = input('Digite qual tarefa deve ser excluida: ')
            afazer.pop(action)
        case '5':
            print('Programa Finalizado')
        case _:
            print('Valor invalido')