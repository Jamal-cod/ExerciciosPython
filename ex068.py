from random import randint
cont = 0
while True:
    pi = str(input('Par ou Ímpar [P/I]? ')).upper()
    pp = int(input('Digite o valor:'))
    pc = randint(1, 11)
    total = pc + pp
    print(f'Você jogou {pp} e o computador {pc}. Total: {total}')
    print('=' * 15)
    if pi in 'P':
        if total % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if pi in 'Ii':
        if total % 2 != 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
    print('-' * 15)
print(f'GAME OVER! \nVocê me venceu {cont} vezes')
