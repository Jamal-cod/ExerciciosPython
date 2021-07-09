p = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
cont = 1
while cont < 10:
    p += r
    cont += 1
    print('{}'.format(p), end='...')
print('FIM')


