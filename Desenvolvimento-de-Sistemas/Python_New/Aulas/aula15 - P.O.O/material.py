# 98 POP
# nome_motorista1 = 'Geraldo'
# carro_motorista1 = 'Renault Kwid'

# class - 'molde do objeto'
# def __init__() - função construtora
# self - 'O próprio objeto'
# PalscalCase - primeira letra de todas as palavras maiusculas (Cliente, Carro)
# obs: camelCase - Sempre começa com letra minúscula (clienteVip)
class Motorista:
    def __init__(self,nome,carro,corCarro,placa):
        self.nome = nome
        self.carro = carro
        self.corCarro = corCarro
        self.placa = placa

motorista1 = Motorista('Geraldo','Renault Kiwd','Rosa pink','1234-top')
motorista2 = Motorista('Victor','Camaro','Preto supremo','camaro-2')
# motorista1.nome = 'Geraldo'
# motorista1.carro = 'Renault Kiwd'

print(motorista1.carro)
print(motorista2.carro)

print(motorista1, type(motorista1))