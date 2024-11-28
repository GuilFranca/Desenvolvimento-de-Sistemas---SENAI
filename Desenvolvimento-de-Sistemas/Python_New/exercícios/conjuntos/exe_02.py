# 2)Duas lojas possuem estoques diferentes de produtos. Encontre os produtos disponíveis em ambas e os exclusivos de cada loja.

loja_1 = {'sonic', 'sonica', 'monic'}

loja_2 = {'mario', 'sonica', 'monic'}

ambas = (loja_1 & loja_2)

exclusivo = (loja_1 ^ loja_2)

print('Produtos presentes em ambas as lojas')

for produtos in ambas:
    print(produtos)

print('Produtos exclusivos de cada loja')

for produtos in exclusivo:
    print(produtos)
