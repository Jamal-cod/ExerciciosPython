v = float(input('Qual o salário atual do funcionário? '))
a = v * 10 / 100 + v
b = v * 15 / 100 + v
if v >= 1.2500:
    print('o salário foi de {} para {}'.format(v, a))
else:
    print('O salário foi de {} para {}'.format(v, b))