# 4)Crie um programa que simule um caixa eletrônico. Peça ao usuário um valor a ser sacado e deduza de um saldo inicial. Caso o usuário tente sacar mais do que o saldo ou insira um valor inválido, trate o erro de forma apropriada. Garanta que o saldo atualizado seja sempre exibido no finally.

saldo = 1500.00
action = 0


print(f'O saldo da sua conta é de {saldo:.2f}')
while action != 3:
    print('Para sacar digite 1')
    print('Para depositar digite 2')
    print('Para fechar programa digite 3')

    action = int(input(''))

    match action:
        case 1:
            try:

                saque = float(input('Digite o valor a ser sacado: '))

                if saque > saldo:
                    raise ValueError("O valor do saque não deve ser maior que o saldo.")
                
                if saque <= 0:
                    raise ValueError('O saque deve ser maior que zero.')
                
                saldo -= saque
                print(f'Saque de R${saque:.2f} efetuado com sucesso.')

            except ValueError as erro:
                print('o valor inserido é invalido')
                print(erro)
                
            finally:
                print(f'Saldo atualizado para: {saldo}')

        case 2:
            try:

                deposito = float(input('Digite o valor a ser depositado: '))
                
                if deposito <= 0:
                    raise ValueError('O deposito deve ser maior quu zero')
                
                saldo += deposito
                print(f'Deposito de R${deposito} efetuado com sucesso.')

            except ValueError as erro:
                print('o valor inserido é invalido')
                print(erro)
            
            finally:
                print(f'Saldo atualizado para: {saldo}')

        case 3:
            print('Caixa encerrado')
