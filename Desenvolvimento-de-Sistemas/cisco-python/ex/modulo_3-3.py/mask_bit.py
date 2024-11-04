numero = 0b1011  # Representação binária do número 11
mascara = 0b0100  # Máscara para verificar o terceiro bit (equivale a 4 em decimal)

# Usando a operação AND para verificar o bit
resultado = numero & mascara

if resultado:
    print("O terceiro bit está definido.")
else:
    print("O terceiro bit não está definido.")
