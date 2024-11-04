x = 4 
# 4 == 100

y = 1
# 1 == 001

a = x & y # 000
b = x | y # 101 == 5
c = ~x  # tricky! 011 == -5 pois inerte todos os outros zeros na frente de 4 11111111111111111111111111111011
d = x ^ 5 # 101
e = x >> 2 # //2 == 1
f = x << 2 # *4 == 16

print(a, b, c, d, e, f)
 
