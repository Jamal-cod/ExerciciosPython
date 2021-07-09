C = float(input('Qual a temperatura em C°? '))
F = C * 1.8 + 32
K = C + 273.15
print('De {}C° para {:.2f}F° \nDe {}C° para {:.2f}K°'.format(C, F, C, K))