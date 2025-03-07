# 2)Crie um sistema de gerenciamento de pedidos para um restaurante. Use classes Pedido, ItemPedido e Cardapio

from classes2 import Cardapio
from classes2 import ItemPedido
from classes2 import Pedido

item1 = ItemPedido('Hamburger',25)
item2 = ItemPedido('lamen',25)

cardapio1 = Cardapio()
cardapio1.adicionar_item(item1)
cardapio1.mostrar_itens()

pedido1 = Pedido()
pedido1.adicionar_pedido(item1,2)
pedido1.adicionar_pedido(item2,2)
pedido1.mostrar_pedido()
pedido1.total_pedido()