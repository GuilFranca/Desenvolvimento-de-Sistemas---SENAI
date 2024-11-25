# Array / LISTAS

# CRUD - Create, Read, Update, Delete

clientes = ['Victor', 'Alan', 'Bruna']
teste = ['texto', 123, True, []]
# clientesAlt = list()

print(type(clientes))
print(teste)

# metodos de uma lista
lista = ['Alvejante', 'Saco de lixo', 'Calmante', 'Serra']

lista.append('Ácido') #append adiciona no final
print(lista)

lista.pop() #pop deleta no final
print(lista)

# indice 0 1 2 3 4 / -5 -4 -3 -2 -1
lista.insert(3, 'Cebola') #insert insere no local desejado
print(lista)

lista.remove('Serra') #deleta pelo valor
print(lista)

del lista[1] #del deleta no local desejado
print(lista)

del lista[:] #deleta a lista toda
print(lista)

lista.clear() #clear deleta a lista toda
print(lista)
