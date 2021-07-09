valores = []
while True:
    c = int(input('Digite um valor: '))
    if c not in valores:
        valores.append(c)
        print('Valor adicionado com sucesso...')
    elif c in valores:
        print('Valor ja adicionado! Vou desconsiderar...')
    i = str(input('Quer continuar [S/N]? ')).upper()
    if i == 'N':
        break
print('-=' * 20)
print(f'Você digitou os valores {sorted(valores)}')
