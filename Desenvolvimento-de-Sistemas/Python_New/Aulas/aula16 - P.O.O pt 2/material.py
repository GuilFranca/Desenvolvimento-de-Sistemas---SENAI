""" 
ENCAPSULAMENTO
(SEM UNDERLINE) = PUBLIC (PUBLICO)
(UMA UNDERLINE) = PROTECTED (NÃO DEVE FORA DA CLASSE)
(DOIS UNDERLINES) = PRIVATE (NÃO É ACESSADO POR OUTRAS PARTES DO CODIGO)

"""

class Carro:
    def __init__(self,nome,cor,placa,peso,marca):
        self.__nome = nome
        self.cor = cor
        self._placa = placa
        self.peso = peso
        self.marca = marca
        self.km_atual = 0
    
    def alterarPlaca(self,placa):
        self.placa = placa
        print(f'Alterei a placa para {self.placa}')

carro1 = Carro('Fiat Uno','Branco','FIATOP',20,'Fiat')
print(carro1)
# dois metodos para apresentar objeto
print(vars(carro1))
carro1.alterarPlaca('ESCADAGOD')
print(carro1.__dict__)