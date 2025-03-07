# 1. Cadastro de Produto
# Você precisa criar um programa que armazene informações de um produto em um dicionário. As informações devem incluir nome, preço e quantidade em estoque. Depois, o programa deve exibir todas as informações do produto.

produto = {
    'nome' : '',
    'preco' : '',
    'qtd' : '',
}

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
qtd = int(input("Digite a quantidade no estoque: "))

produto.update({
    'nome' : nome,
    'preco' : preco,
    'qtd' : qtd
})

print(produto)