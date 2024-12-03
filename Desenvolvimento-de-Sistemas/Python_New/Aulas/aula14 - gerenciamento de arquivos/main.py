# arquivo = 'main.txt\pastatal'
arquivo = 'main.txt'

# MODOS DO TEXTIOWRAPPER
# w (escrita)
# r (read)
# x (criação)
# t (modo texto)
# w+, r+ (escrita e leitura)
# b (binario)

# Metodo 1
# leitura = open(arquivo,'w') # 'w' writeble quer dizer que á pra escrever
# leitura.close()

# escrito = input('Digite algo: ')

# Metodo 2
with open(arquivo,'w+') as leitura:
    # write - escreve uma linha
    # writelines - escreve multiplas linhas
    # seek - move cursor
    # leitura.write(escrito)
    leitura.write('Line1 \n')
    leitura.write('Line2 \n')
    leitura.seek(0,0)
    leitura.writelines(
        ('Linha 2\n', 'Linha 3\n', 'Linha 4\n')
    )

with open(arquivo,'r') as leitura:
    print(leitura.read())
    print(leitura.readline().strip)

# print(arquivo)
# print(leitura)