p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
total = 0
c = 10
while c != 0:
    total += c
    while cont <= total:
        p1 += r
        cont += 1
        print('{}...'.format(p1), end='')
    print('PAUSA')
    c = int(input('Quer adicionar quantos mais termos? '))



