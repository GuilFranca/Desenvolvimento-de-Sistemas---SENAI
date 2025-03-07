# print(10 / 0)

# lista = [0, 1, 2, 3] IndexError
# print(lista[4])

# dicionario = {'chave' : 'valor'} KeyError
# print(dicionario['victor'])

try:
    NUM_1 = 18
    NUM_2 = 5

    NUM_3 = NUM_1 / NUM_2

    print(NUM_3)

    listaBacana = [NUM_3]
    print(listaBacana[0])

    # RAISE - chama um erro para acontecer
    raise KeyError

except ZeroDivisionError as erro:
    print("Não pode dividir por zero")
    print(erro)
except IndexError as erro:
    print("Erro elemento da lista")
    print(erro)
except Exception:
    print("erro desconhecido")   
finally:
    print('EXECUTEI O PROGRAMA!')

print('Que legal!')
