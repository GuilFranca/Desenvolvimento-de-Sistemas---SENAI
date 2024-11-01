# Solicita a quantidade de blocos disponível
blocos = int(input("Digite o número de blocos disponíveis: "))

# Variáveis para contar o número de camadas e blocos usados
camada = 0
blocos_usados = 0

# Loop para calcular o número de camadas que podem ser construídas
while blocos_usados + (camada + 1) <= blocos:
    camada += 1
    blocos_usados += camada

print("O número máximo de camadas da pirâmide é:", camada)
