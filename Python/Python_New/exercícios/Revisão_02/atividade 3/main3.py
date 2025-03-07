# 3)Crie uma classe Pessoa com os atributos nome e idade. Adicione um método para retornar a data de nascimento.

from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def data_nascimento(self):
        print(self.ano_atual - self.idade)

p1 = Pessoa('Gui',20)
p1.data_nascimento()