def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
       :param num: O número a ser calculado.
       :param show: (opcional) mostar ou não o cálculo.
       :return: O valor do fatorial de um número num.
    """
    from time import sleep
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == False:
        print(f'O fatorial de {num} é {f}')
    else:
        for c in range(num, 0, -1):
            print(c, end=' ', flush=True)
            sleep(0.5)
            if c > 1:
                print('x', end=' ')
            if c <= 1:
                print(f'= {f}', end='')



print('-' * 25)

help(fatorial)