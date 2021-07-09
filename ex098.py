from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    cont = i
    if p == 0:
        p = 1
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.5)
        print()
        print('-=' * 15)

    if i > f:
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print()
        print('-=' * 15)

contador(1, 10, 1)
contador(10, 1, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
