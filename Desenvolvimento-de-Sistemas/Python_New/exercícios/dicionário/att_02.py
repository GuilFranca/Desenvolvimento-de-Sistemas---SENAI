# 2. Agenda de Contatos
# Crie um programa para armazenar números de telefone. O usuário deve poder adicionar novos contatos (nome como chave e número como valor). Depois, o programa deve exibir todos os contatos cadastrados. Obs: O salvamento deverá parar apenas quando o usuário digitar "finalizar"

lista = {
    
}

num = 0

while num != -1:
    nome = input("Digite o nome do contato: ")
    num = int(input("Digite um número de telefone: "))
    lista.setdefault(nome, num)
    print(lista)

    
