numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista: ", numbers) # imprimindo o conteúdo original da lista.

numbers[0] = 111
print("\nNovo conteúdo da lista: ", numbers[0]) # Conteúdo atual da lista

numbers[1] = numbers[4]
print("Novo conteúdo da lista: ", numbers)

print("\nList length: ", len (numbers)) # Imprimindo o comprimento da lista

del numbers[1]
print(len (numbers))
print(numbers)

# numbers[4] = 1
# print(numbers[4])

numbers = [111, 7, 2, 1]
print(numbers[-1]) # É o último elemento da lista
 