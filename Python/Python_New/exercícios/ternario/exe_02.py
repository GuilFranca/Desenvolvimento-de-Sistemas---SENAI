# 2)Faça um algoritmo que avalie se o usuario e senha cadastrados e 
# se não tiver, printe uma falha
# senao printe que deu tudo certo
# (considerar que usuario e senha sejam ''ADM')

def ex2():
    usuario_cadastrada = 'ADM'
    senha_cadastrada = 'ADM'

    usuario = input('Qual é o usuário: ')
    senha = input('Qual é a senha: ')

    print('USUÁRIO CORRETO!') if usuario == usuario_cadastrada else print('USUÁRIO INCORRETO')

    print('SENHA CORRETA!') if senha == senha_cadastrada else print('SENHA INCORRETA')

ex2()