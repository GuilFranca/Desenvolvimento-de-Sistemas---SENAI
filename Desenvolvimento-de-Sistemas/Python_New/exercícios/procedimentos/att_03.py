# 3) faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2,3 e 5.

# def media(n1, n2, n3):
#     media_aluno = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)
#     print(f"A média do aluno é: {media_aluno:.2f}")

# n1 = float(input("Digite sua nota da N1: "))
# n2 = float(input("Digite sua nota da N2: "))
# n3 = float(input("Digite sua nota da N3: "))

# media(n1, n2, n3)

notas = [0,0,0]

for i in range(0,3,1):
    nota = float(input(f"Digite a {i+1}º nota: "))
    notas[i] = nota

media_final = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 5)) / (2 + 3 + 5)

print(f"A média final do aluno é de {media_final}")

print(notas)