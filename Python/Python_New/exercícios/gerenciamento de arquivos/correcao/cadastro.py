import json

def cadastrarUsuario():
    print('-=-=CADASTRO=-=-')

    nome = input('Digite seu nome: ')
    login = input('Digite seu login (email): ')
    cpf = int(input('Digite seu cpf: '))

    while True:
        senha = input('Digite sua senha: ')
        c_senha = input('confirme sua senha: ')

        if senha == c_senha:
            break
        else:
            print('Senha não bate na confirmação, tente novamente.')
    

    usuario = {
            'nome' : nome,
            'login' : login,
            'cpf' : cpf,
            'senha' : senha
    }

    with open('dados.json','w',encoding='utf8') as leitura:
        json.dump(
            usuario,
            leitura,
            indent=2
        )


import json

# Nome do arquivo JSON
arquivo_json = 'usuarios.json'

# Carregar o conteúdo do arquivo JSON
try:
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    dados = {"usuarios": []}  # Cria uma estrutura padrão se o arquivo não existir

# Novo usuário a ser adicionado
novo_usuario = {
    "nome": "João Silva",
    "email": "joao.silva@example.com",
    "idade": 25
}

# Verificar se a chave "usuarios" existe e é uma lista
if "usuarios" in dados and isinstance(dados["usuarios"], list):
    dados["usuarios"].append(novo_usuario)
else:
    dados["usuarios"] = [novo_usuario]  # Cria a lista se não existir

# Salvar os dados atualizados de volta no arquivo JSON
with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("Usuário adicionado com sucesso!")
