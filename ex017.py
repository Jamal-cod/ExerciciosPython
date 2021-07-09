import math
c1 = float(input('Qual o valor de um cateto? '))
c2 = float(input('Qual o valor do outro cateto? '))
h = math.hypot(c1, c2)
print('A soma dos catetos {} e {} é igual a {:.2f}'.format(c1,c2, h))