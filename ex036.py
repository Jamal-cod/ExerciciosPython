x = float(input('Qual o valor da casa? '))
y = float(input('Qual o salário do comprador? '))
z = int(input('Em quantos anos vai ser pago? '))
tp = (x / z) / 12
v = (30 * y) / 100
if tp > v:
    print('Pra pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(x, z, tp))
    print('Empréstimo NEGADO')
elif tp < v:
    print('Pra pagar uma casa de R$ {} em {} anos, a prestação será de R${:.2f}'.format(x, z, tp))
    print('Empréstimo CONCEDIDO')