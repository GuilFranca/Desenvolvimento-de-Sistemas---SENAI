year = int(input("Digite um ano: "))

if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} é um ano bissexto")
    else:
        print(f"{year} é um ano comum")
