lista = list()
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]? ')).upper()[0]
    if resp == 'N':
        break
print(f'{"NOME":<10}{"NOTA":}')
print('-' * 20)
for l in lista:
    print(f'{l[0]:<10}{l[2]}')
print('-' *20)
