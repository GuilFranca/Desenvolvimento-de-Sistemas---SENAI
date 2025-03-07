# 2)Programe um algoritmo onde podemos colocar um valor em reais e logo a pós perguntar qual moeda deseja converter ( Dólares, Ienes ou euro) e logo após isso fazermos a conversão

def converter():
    valor = float(input("Digite o valor: "))
    moeda = input("Converter para (dolar, iene, euro): ")

    convertercao = {
        'dolar' : valor * 0.17,
        'iene' : valor * 25.33,
        'euro' : valor * 0.16
    }

    print(f'\nSeu valor em R$: {valor}')
    print(f'Seu valor convertido para {moeda}: {convertercao[moeda]}')

converter()