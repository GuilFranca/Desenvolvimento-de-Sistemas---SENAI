# 3) faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2,3 e 5.

def media(n1, n2, n3):
    media_aluno = ((n1 * 2) + (n2 * 3) + (n3 * 4)) / (2 + 3 + 4)
    print(f"A média do aluno é: {media_aluno:.2f}")

n1 = float(input("Digite sua nota da N1: "))
n2 = float(input("Digite sua nota da N2: "))
n3 = float(input("Digite sua nota da N3: "))

media(n1, n2, n3)