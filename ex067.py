c = 1
t = 0
while True:
    i = int(input('Digite um valor: '))
    print(f'TABUADA de {i}')
    print('-' * 15)
    while t < 10:
        t += 1
        print(f'{i} x {t} = {i*t}')
    print('-' * 15)
    if i < 0:
        break
print('Programa tabuada encerrado. Volte sempre.')
