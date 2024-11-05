my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for i in my_list:
    if i not in unique_list:  # verifica se o elemento já está na lista auxiliar
        unique_list.append(i)  # adiciona apenas se não estiver presente

print("A lista com os elementos exclusivos aqui:")
print(unique_list)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Remover duplicatas usando um set
my_list = list(set(my_list))

print("A lista com os elementos exclusivos aqui:")
print(my_list)
