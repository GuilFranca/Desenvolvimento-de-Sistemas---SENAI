# 3) Faça o jogo da forca em python utilizando o Set() como base!

# PYTHON - SECRETA
# _ _ a _ _ b - 6 TENTATIVAS
# QUAL LETRA VAI TENTAR?
tentativas = 6
palavra_secreta = 'SEXTAFEIRA13'
letras_p_secreta = set(palavra_secreta)
letras_tentadas = set()

while tentativas > 0 and letras_p_secreta:
    # EXIBIR A PALAVRA
    palavra_exibida = []
    for letra in palavra_secreta:
        if letra in letras_tentadas:
            palavra_exibida.append(letra)
        else:
            palavra_exibida.append('_')
        
    print("Palavra:",' '.join(palavra_exibida))

    # PEDIR UMA LETRA
    letra = input('Digite uma letra: ').upper()

    # ADICIONAR NAS TENTATIVAS
    letras_tentadas.add(letra)

    # VERIFICAR ACERTO
    if letra in letras_p_secreta:
        print(f'BOA! a letra {letra} está na palavra!')
        letras_p_secreta.remove(letra)
    else:
        print(f'OH NÃO :( , a letra {letra} não existe')
        tentativas -= 1
        print(f'Vidas restantes: {tentativas}')
    
# MENSAGEM DE PERDA / OU GANHO
# tentativas > 0
if not letras_p_secreta:
    print(f'VOCÊ GANHOU O JOGO! palavra secreta {palavra_secreta}')
else:
    print(f'GAME OVER! a palavra secreta {palavra_secreta}')