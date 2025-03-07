# 1)Implemente um sistema de gerenciamento de estoque que inclua classes Produto, Estoque e métodos para adicionar, remover e verificar produtos.

from classes1 import Estoque
from classes1 import Produto

galpao = Estoque('Galpão Central')
# print(galpao.__dict__)

galpao.inserir_produto('Pão',5)
galpao.inserir_produto('Miojo',10)
galpao.listar_produtos()

print()

galpao.verificar_produto('Pão')

print()

galpao.remover_produto('Pão')
galpao.listar_produtos()