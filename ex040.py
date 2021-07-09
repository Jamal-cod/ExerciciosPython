n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
x = (n1 + n2) / 2
print('Sua média foi {}'.format(x))
if x < 5.00:
    print('REPROVADO')
elif x > 5.00 and x < 6.9:
    print('RECUPERAÇÃO')
elif x >= 7.00:
    print('APROVADO')