alunosPt1 = ['Michal', 'Jackson', 'Da Silva']
alunosPt2 = ['Ihiiiiiiiii', 'uuhoooooooooo', 'Bilidin']

alunosPt3 = alunosPt1 + alunosPt2
print(alunosPt3)

alunosPt1.extend(alunosPt2)
print(alunosPt1)

print(alunosPt2)

print(len(alunosPt1)) #len conta os elementos dentro da array

for nome in alunosPt1:
    print(nome)