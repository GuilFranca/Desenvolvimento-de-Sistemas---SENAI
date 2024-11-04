income = float(input("Entre com os rendimentos anuais "))

limite = 85528

if income < limite:
    tax = income * 0.18 - 556.02
elif income > limite:
    tax = (income - limite) * 0.32 + 14839

tax = round(tax, 0)

if tax <= 0:
    tax = 0

print("A taxa é:", tax, "thalers") 
 