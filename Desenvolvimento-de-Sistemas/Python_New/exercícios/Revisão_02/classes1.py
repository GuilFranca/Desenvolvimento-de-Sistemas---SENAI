# 1)Implemente um sistema de gerenciamento de estoque que inclua classes Produto, Estoque e métodos para adicionar, remover e verificar produtos.

class Produto:
    def __init__(self,descricao,qtd):
        self.descricao = descricao
        self.qtd = qtd

class Estoque:
    def __init__(self,nome):
        self.nome = nome
        self.estoque = []

    def inserir_produto(self,descricao,qtd):
        self.estoque.append(Produto(descricao,qtd))

    def listar_produtos(self):
        for produto in self.estoque:
            print(produto.descricao,produto.qtd)
    
    def remover_produto(self,descricao):
        for produto in self.estoque:
            if produto.descricao == descricao:
                self.estoque.remove(produto)
    
    def verificar_produto(self,descricao):
        for produto in self.estoque:
            if produto.descricao == descricao:
                print(produto.descricao, produto.qtd)

