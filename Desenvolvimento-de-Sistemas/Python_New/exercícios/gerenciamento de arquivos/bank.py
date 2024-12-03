import json

banco_usuarios = {
    'gui_123': {
        'nome': 'Guilherme',
        'senha': '123'
    },

    'quel_123': {
        'nome': 'Raquel',
        'senha': '456'
    }
}

with open('dados.json','w',encoding='utf8') as leitura:
    json.dump(
        banco_usuarios,
        leitura,
        indent=2
    )

with open('dados.json','r',encoding='utf8') as leitura:
    banco_dados_usuarios = json.load(leitura)
    print(banco_dados_usuarios)