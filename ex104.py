def leiaInt():
    red = "\033[1;31m"
    print('-' * 20)
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            n = int(n)
            print(f'Voce digitou o número {n}')
            break
        else:
            print(f'\033[0;31;mERRO! Digite um número inteiro válido\033[m')

leiaInt()