from datetime import datetime
x = datetime.now()
at = x.year
cont = 0
val = 0
for c in range(1, 8):
    a = int(input('Em que ano a pessoa {} nasceu?'.format(c)))
    idade = at - a
    if idade >= 21:
        cont += 1
    else:
        val += 1
print('Ao todo tivemos {} pessoas maiores de idade \n'
      'E também tivemos {} pessoas menores de idade'.format(cont, val))