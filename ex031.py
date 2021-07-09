km = int(input('Quantos km até o destino da sua viagem? '))
if km <= 200:
    p = 0.50*km
    print('A sua passagem vai custar R${}'.format(p))
else:
    p2 = 0.45*km
    print('A sua passagem vai custar R${}'.format(p2))