try:
    value = input("Digite um valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada ruim...")
except ZeroDivisionError:
    print("Entrada muito ruim...")
except TypeError:
    print("Muito, muito ruim entrada...")
except:
    print("Booo!")
 
