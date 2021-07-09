produtos = ('Leite', 3,
            'Coca', 4,
            'Calabresa', 15)
print(f'{"LISTAGEM DE PREÇO":^40}')
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f'{produtos[n]:.<30}', end='R$')
    else:
        print(f'{produtos[n]:>6.2f}')