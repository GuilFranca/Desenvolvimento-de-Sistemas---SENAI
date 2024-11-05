temps = [[0.0 for h in range(24)] for d in range(31)]

#
# A matriz é magicamente atualizada aqui.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura média ao meio-dia:", average)
 
