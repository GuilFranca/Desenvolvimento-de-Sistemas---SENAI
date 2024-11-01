# secret_word = "chupacabra"
# chute = input("Adivinhe a palvra chave: ")

# while chute != secret_word:
#     chute = input("Digite outra palavra: ")

# print(f"Você acertou a palavra secreta é: {secret_word}")

while True:
    palavra = input("Digite uma palavra: ")
    if palavra == "chupacabra":
        print("Você saiu do loop com sucesso")
        break
