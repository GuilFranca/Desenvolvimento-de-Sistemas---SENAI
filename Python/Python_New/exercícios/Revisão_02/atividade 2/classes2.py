# 2)Crie um sistema de gerenciamento de pedidos para um restaurante. Use classes Pedido, ItemPedido e Cardapio

class ItemPedido:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        self.qtd = None

class Cardapio:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self,item):
        self.itens.append(item)
    
    def remover_item(self,item):
        self.itens.remove(item)

    def mostrar_itens(self):
        for item in self.itens:
            print(item.nome, item.preco)

class Pedido:
    def __init__(self):
        self.pedidos = []
    
    def adicionar_pedido(self,item,qtd):
        self.pedidos.append(item)
        item.qtd = qtd
    
    def remover_pedido(self,item):
        self.pedidos.remove(item)

    def mostrar_pedido(self):
        for item in self.pedidos:
            print(item.nome, item.qtd)
    
    def total_pedido(self):
        total = 0
        for item in self.pedidos:
            total = total + (item.preco * item.qtd)
        print(total)