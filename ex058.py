from random import randint
ale = randint(1, 10)
cont = 0
c = 0
print('Vou pensar em um número pra você adivinhar...')
while c != ale:
    c = int(input('Qual número eu pensei? '))
    cont += 1
    if c < ale:
        print('Maior...Tente novamente')
    elif c > ale:
        print('Menor...tente novamente')
print('Você precisou de {} palpites para me vencer'.format(cont))
print('-----FIM-----')
