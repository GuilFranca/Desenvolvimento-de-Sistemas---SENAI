# 2)Crie um dicionário com informações sobre um aluno (por exemplo, nome, idade, notas). Em seguida, solicite ao usuário uma chave para acessar no dicionário. Caso a chave não exista, trate o erro e informe quais chaves estão disponíveis.

aluno = {
    'nome' : 'Guilherme',
    'idade' : 20,
    'media' : 9.5
}

try:
    chave = input('Solicite uma chave para acessar o dicionário: ')
    print(aluno[chave])

except KeyError as erro:
    print('Erro de chave')
    print(erro)
