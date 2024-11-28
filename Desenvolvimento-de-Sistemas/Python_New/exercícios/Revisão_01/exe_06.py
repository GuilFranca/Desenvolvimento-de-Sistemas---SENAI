# 6)Sucessor e antecessor, faça uma aplicação que colete um número digitado pelo usuário e logo em seguida mostre em ordem: o numero anterior a ele, o próprio número escolhido e o número sucessor a ele

# Coletar o número digitado pelo usuário
numero = int(input("Digite um número: "))

# Criar o dicionário com os valores
numeros = {
    "Anterior": numero - 1,
    "Escolhido": numero,
    "Sucessor": numero + 1
}

# Mostrar os resultados
for chave, valor in numeros.items():
    print(f"{chave}: {valor}")
