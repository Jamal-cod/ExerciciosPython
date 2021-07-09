a = int(input('Digite um ano: '))
if a % 4==0 and a % 100 != 0 or a % 400 == 0:
    print(' O ano {} É BISSEXTO'.format(a))
else:
    print('O ano {} NÃO É BISSEXTO'.format(a))