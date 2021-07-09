def maior(*num):
    max = 0
    for n in num:
        if n == 0:
            max = n
        else:
            if n > max:
                max = n
    print('Analisando os valores passados...')
    print(f'{num} '
          f'\nforam informados {len(num)} valores ao todo. '
          f'\nO maior valor informado foi {max}')
    print('-='*20)
maior(4, 7, 10)