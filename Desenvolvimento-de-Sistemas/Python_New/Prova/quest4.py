# 4)Crie duas classes:
# 1 Autor, com os atributos:  Nome, nacionalidade e livros
# 2 Livro, com os atributos: titulo, ano e autor
# Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
# Imprima o nome do autor e a lista dos seus livros.

class Autor:
    def __init__(self,nome,nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []
    
    def adicionar_livro(self,livro):
        self.livros.append(livro)
    
    def mostrar_livros(self):
        for livro in self.livros:
            print(f'{livro.titulo} : {livro.ano}')

    def mostrar_autor(self):
        print(f'Autor: {self.nome}')
        print('Livros: ')
        self.mostrar_livros()

class Livro:
    def __init__(self,titulo,ano):
        self.titulo = titulo
        self.ano = ano
        self.autor = None


a1 = Autor('Guilherme','Brasileiro')

l1 = Livro('Amostradinho',2024)
l2 = Livro('Lá ele',2023)

a1.adicionar_livro(l1)
a1.adicionar_livro(l2)

a1.mostrar_autor()