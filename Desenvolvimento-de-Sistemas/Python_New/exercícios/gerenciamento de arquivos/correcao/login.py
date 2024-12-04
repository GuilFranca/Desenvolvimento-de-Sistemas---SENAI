import json

def loginUsuario():
    print('-=-=LOGIN=-=-')

    login = input('Login: ')
    senha = input('Senha: ')

    with open('dados.json','r',encoding='utf8') as leitura:
        dados = json.load(leitura)
        c_login = dados['login']
        c_senha = dados['senha']
        c_nome = dados['nome']
    
    if c_login == login and c_senha == senha:
        print(f'Seja bem vindo(a), {c_nome}')
    else:
        print('Usuário ou Senha incorretos.')

