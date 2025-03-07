user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

# Solicita que o usuário insira uma palavra
# e atribua-a à variável user_word.

for letter in user_word:
    if letter in "AEIOU":
        continue
    # Preenchao corpo do loop for.
    print(letter)
