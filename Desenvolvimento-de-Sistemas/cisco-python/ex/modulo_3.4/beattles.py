# etapa 1: criar uma lista vazia chamada beatles
beatles = []

# etapa 2: adicionar cada membro individualmente
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# etapa 3: usar loop para adicionar membros
for i in range(2):
    add = input("Digite o nome dos integrantes da banda: ")
    beatles.append(add)

# etapa 4: remover Stu Sutcliffe e Pete Best da lista
del beatles[4]
del beatles[3]

# etapa 5: adicionar Ringo Starr ao início da lista
beatles.insert(0, "Ringo Starr")

print(beatles)
