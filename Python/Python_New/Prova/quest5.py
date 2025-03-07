# 5)Implemente uma função chamada calculadora que:Receba dois números e uma operação (adição, subtração, multiplicação ou divisão).Retorne o resultado da operação.Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json

import json
import os

def soma(n1,n2):
    resultado = (n1 + n2)
    print(f'{n1} + {n2} = {resultado}')
    exportar_dados(n1,n2,operacao)

def subtracao(n1,n2):
    resultado = (n1 - n2)
    print(f'{n1} - {n2} = {resultado}')
    exportar_dados(n1,n2,operacao)

def multiplicacao(n1,n2):
    resultado = (n1 * n2)
    print(f'{n1} * {n2} = {resultado}')
    exportar_dados(n1,n2,operacao)

def divisao(n1,n2,operacao):
    if n1 == 0 or n2 == 0:
        print('Não é possível dividir por ZERO!')
    else:
        resultado = (n1 / n2)
        print(f'{n1} {operacao} {n2} = {resultado}')
        exportar_dados(n1,n2,operacao)

def exportar_dados(n1,n2,operacao):
    dados_calculadora = {
        'numero 1' : n1,
        'numero 2' : n2,
        'operacao' : operacao
    }
    if os.path.exists('dados.json'):
        with open('dados.json','r', encoding='utf8') as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                dados = []
    else:
        dados = []
            
    dados.append(dados_calculadora)

    with open('dados.json','w', encoding='utf8') as f:
        json.dump(dados,f,indent=2)

operador = 0

while operador != 5:
    print('-=-=-=CALCULADORA=-=-=-')
    print('1 - ADIÇÃO')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')
    print('5 - SAIR')
    operador = int(input())

    match operador:
        case 1:
            numer_1 = float(input('Digite o primerio NÚMERO: '))
            numer_2 = float(input('Digite o segundo NÚMERO: '))
            operacao = '+'
            soma(numer_1,numer_2)
        
        case 2:
            numer_1 = float(input('Digite o primerio NÚMERO: '))
            numer_2 = float(input('Digite o segundo NÚMERO: '))
            operacao = '-'
            subtracao(numer_1,numer_2)
        
        case 3:
            numer_1 = float(input('Digite o primerio NÚMERO: '))
            numer_2 = float(input('Digite o segundo NÚMERO: '))
            operacao = '*'
            multiplicacao(numer_1,numer_2)

        case 4:
            numer_1 = float(input('Digite o primerio NÚMERO: '))
            numer_2 = float(input('Digite o segundo NÚMERO: '))
            operacao = '/'
            divisao(numer_1,numer_2)

        case 5:
            print('PROGRAMA ENCERRADO!')