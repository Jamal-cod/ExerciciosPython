print('=' * 5, 'LOJAS JONES', '=' * 5)
preço = float(input('Qual o preço da suas compras? '))
print('FORMAS DE PAGAMENTO')
print('[1] À vista dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] Em até 2x no cartão')
print('[4] 3x ou mais no cartão')
pagamento = int(input('Qual a forma de pagamento? '))
if pagamento == 1:
    d1 = (preço * 10) / 100
    print('Sua compra de R${} vai custar R${} no final. '.format(preço, preço - d1))
elif pagamento == 2:
    d2 = (preço * 5) / 100
    print('Sua compra de R${} no final vai custar R${}.'.format(preço, preço - d2))
elif pagamento == 3:
    d3 = preço / 2
    print('Sua compra de 2x de R${} \nVai custar R${:.2f} no final.'.format(d3, preço))
elif pagamento == 4:
    d = int(input('Quantas parcelas? '))
    d4 = preço / d
    juros = (preço * 20) / 100 + preço
    print('Sua compra de {}x de R${:.2f} \nDe R${} sua compra no final vai para {}'.format(d, d4, preço, juros))
else:
    print('Forma de pagamento INVÁLIDA, tente novamente')
pr