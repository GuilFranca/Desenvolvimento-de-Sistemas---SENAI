# 1)Encontrar alunos que cursam apenas uma disciplina dado as disciplinas:
# -matematica com os nomes dos alunos que fazem Matemática
# -fisica com os nomes dos alunos que fazem Física
# Encontre os alunos que fazem apenas uma das disciplinas.

matematica = {'gui', 'roger', 'quel'}

fisica = {'gui', 'mario', 'london'}

apenas_uma = (matematica ^ fisica)

for aluno in apenas_uma:
    print(aluno)