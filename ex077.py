palavras = ('cachorro', 'palavra', 'doguinho', 'lanchonete')
for pal in palavras:
    print(f'\nNa palavra {pal} temos ', end='')
    for letra in pal:
        if letra in 'aeiou':
            print(letra, end=' ')