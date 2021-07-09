dias = int(input('Por quantos dias foi alugado o carro? '))
km = float(input('Quantos km o carro percorreu? '))
a = dias * 60
b = km * 0.15
c = a + b
print('O preço final fica por: R${}'.format(c))