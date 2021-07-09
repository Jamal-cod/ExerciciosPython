import datetime
a = int(input('Ano de nascimento: '))
x = datetime.datetime.now()
x1 = x.year
print('Quem nasceu em {} tem {} em {}'.format(a, x1 - a, x1))
if x1 - a < 18:
    print('O seu alistamento é em {}'.format(x1 + (18-(x1-a))))
elif x1 - a > 18:
    print('O ano do seu alistamento foi a {} ano(s) atrás \nSe ainda não se alistou, corra atrás! '.format(x1 - a - 18))
elif x1 - a == 18:
    print('Se aliste imediatamente')


