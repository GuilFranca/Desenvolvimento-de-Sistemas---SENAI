num = int(input("Digite um número: "))
vezes = int(input("Até quanto multiplicar: "))

for i in range(vezes):
    print(f"{num} X {i + 1} = {num * (i + 1)}")
