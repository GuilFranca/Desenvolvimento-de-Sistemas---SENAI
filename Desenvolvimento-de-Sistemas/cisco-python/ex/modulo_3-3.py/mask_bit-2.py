numero = 0b1010  # Número inicial (10 em decimal)
mascara = 0b0100  # Máscara para o terceiro bit

# Definindo o terceiro bit como 1
numero |= mascara

print(bin(numero))  # Saída: 0b1110 (14 em decimal)
print(numero)
