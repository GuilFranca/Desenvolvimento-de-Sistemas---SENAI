"""
4)Crie uma classe Aluno que tenha os atributos nome, notas (uma lista) e métodos para calcular a média e verificar se o aluno foi aprovado (média >= 7). Todo aluno criado deverá ser adicionado a um Json.

1 - Criar o aluno (objeto) / atributos Nome: Notas:
2 - Calculo de média é um método do aluno.
3 - Verificar se ele passou ou não.
4 - Calcular a media, criar objetos.
5 - Verificar se existe um aluno anterior.
6 - Exportar para um json.
"""
import json
import os

class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self.__notas = []
    
    @property
    def notas(self):
        return self.__notas

    def adicionar_notas(self,nota):
        self.__notas.append(nota)
    
    def calcular_media(self):
        if self.notas:
            return sum(self.__notas) / len(self.__notas)
        else:
            return 0
        # total = 0
        # contador = 0
        # for nota in self.__notas:
        #     total = total + nota
        #     contador += 1
        # return total / contador
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        
        if media >= 7:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
    
    def exportar_json(self):
        dados_alunos = {
            'nome' : self.nome,
            'notas' : self.notas,
            'media' : self.calcular_media(),
            'aprovacao' : self.verificar_aprovacao()
        }
    
        # Se arquivo existe! se sim salva dados.
        # Se não, dados vaazio.
        if os.path.exists('dados.json'):
            with open('dados.json','r') as arquivo:
                try:
                    dados = json.load(arquivo)
                except json.JSONDecodeError:
                    dados = []
        else:
            dados = []
        
        dados.append(dados_alunos)

        with open('dados.json','w',encoding='utf8') as arquivo:
            json.dump(dados,arquivo,indent=2)



aluno1 = Aluno('Victor')
aluno1.adicionar_notas(8)
aluno1.adicionar_notas(5)
print(aluno1.notas)
print(aluno1.calcular_media())
aluno1.exportar_json()

aluno2 =Aluno('Bruna')

print(vars(aluno1))
print(vars(aluno2))
