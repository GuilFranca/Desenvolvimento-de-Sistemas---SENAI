# DICIONARIO
# CHAVE E VALOR

usuario = {
    #chave : valor
    'nome' : 'Victor',
    'email' : 'emailtop@gmail.com',
    'senha' : '!123456',
    'cpf' : '064.121.881-85',
    'vip' : True,
    'endereco' : [
        {
            'rua' : '13',
            'cidade' : 'Ceilandia',
            'estado' : 'DF'
        }
    ]
}

# print(usuario['nome'])
# print(usuario, type(usuario))

# arquitetura de dic facilita o gerenciamento de dados e busca por eles (obs: até mesmo o crud)

# pesquisa = input("Digite o que quer achar: ")
# print(usuario[pesquisa])

# METODOS DICIONARIO
# len - QUANTAS CHAVES TEM NO DICIONARIO
# keys - RETORNA AS CHAVES
# values - RETORNA OS VALORES
# items - RETORNA CHAVES E VALORES
# setdefault - ADICIONA VALOR SE A CHAVE NÃO EXISTE
# get - BUSCA CHAVE
# pop - APAGA UMA CHAVE ESPECÍFICA (del)
# popitem - APAGA A ULTIMA CHAVE
# update - ATUALIZA UM DICIONARIO
# sum - SOMA OS VALORES OU CONCATENA

print(len(usuario))
print(list(usuario.keys()))
print(list(usuario.values()))
print(list(usuario.items()))

usuario.setdefault('saldo', 0)
print(usuario)

usuario.get('nome')
print(usuario.get('nome'))

usuario.pop('nome')
print(usuario)

usuario.popitem()
print(usuario)

usuario.update({
    'nome' : 'Victor',
    'email' : 'victor.roho@gmail.com'
})
print(usuario)

soma = sum(usuario.values())
print(soma)