import datetime
n1 = int(input('Ano de nascimento do atleta: '))
n2 = datetime.datetime.now()
n3 = n2.year
print('Idade do atleta: {} anos'.format(n3-n1))
if n3 - n1 <= 9:
    print('Classificação: MIRIM')
elif n3 - n1 > 9 and n3 - n1 <= 14:
    print('Classificação: INFANTIL')
elif n3 - n1 > 14 and n3 - n1 <= 19:
    print('Classificação: JUNIOR')
elif n3 - n1 == 20:
    print('Classificação: SÊNIOR')
elif n3 - n1 > 20:
    print('Classificação: MASTER')

