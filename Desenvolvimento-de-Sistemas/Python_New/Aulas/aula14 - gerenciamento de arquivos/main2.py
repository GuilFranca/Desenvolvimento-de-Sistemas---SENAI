import json
# Padroniza os dados
usuario = {
    'nome' : 'Emilia',
    'idade' : 15,
    'cep' : '8888888-99'
}

# encoding = 'utf8' - serve para unificar todos os padrões de caracteres.

# criar o json
# json.dump = joga os dados
with open('dados.json', 'w', encoding='utf8') as leitura:
    json.dump(
        usuario,
        leitura,
        indent=2 # quebra linha 2 é a qtd de espaços
    )
    # leitura.write('ATENÇÃO!!')

with open('dados.json', 'r', encoding='utf8') as leitura:
    pessoa = json.load(leitura)
    print(pessoa)