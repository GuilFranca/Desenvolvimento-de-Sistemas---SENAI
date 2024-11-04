# Você pode estar familiarizado com as leis de De Morgan. Eles dizem que:
# A negação de uma conjunção é a disjunção das negações.
# A negação de uma disjunção é a conjunção das negações.

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# 1 == True e 0 == False

i = 1
j = not not i
 
print(j)