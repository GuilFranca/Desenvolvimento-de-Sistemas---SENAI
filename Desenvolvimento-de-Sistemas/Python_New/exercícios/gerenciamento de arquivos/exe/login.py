import json

# Carregar o conteúdo do arquivo json
with open('dados.json','r',encoding='utf8') as leitura:
    banco_dados_usuarios = json.load(leitura)

operador = 0

while operador != 3:

    print('-=-=DIGITE=-=-')
    print('-=1 para LOGAR=-')
    print('-=2 para CADASTRAR-SE=-')
    print('-=3 para SAIR=-')

    operador = int(input(''))

    match operador:
        
        case 1:
            login_input = input('Login: ')
            senha_input = input('Senha: ')

            if login_input in banco_dados_usuarios:
                if banco_dados_usuarios[login_input]['senha'] == senha_input:
                    print('Senha correta')
                else:
                    print('Senha incorreta')
            else:
                print('Usuário não encontrado')
        
        case 2:
            print('FAÇA O SEU CADASTRO')
            nome_input = input('Nome: ')
            login_input = input('Login: ')
            senha_input = input('Senha: ')

            banco_dados_usuarios[login_input] = {"nome": nome_input,"senha": senha_input}

            with open('dados.json','w',encoding='utf8') as leitura:
                json.dump(
                    banco_dados_usuarios,
                    leitura,
                    indent=2
                )
        
        case 3:
            print('Programa Finalizado...')




