n = float(input('Preço do produto: R$'))
d = n*5/100
f = n - d
print('Com 5% de desconto esse produto fica por R${:.2f}'.format(f))