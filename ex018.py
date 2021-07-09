import math
ang = float(input('Qual o valor do ângulo? '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('O seno de {} é {:.2f}\nO cosseno {:.2f}\ne a tangente {:.2f}'.format(ang, s, c, t))