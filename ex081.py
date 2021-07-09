count = 0
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    c = str(input('Quer continuar [S/N]? ')).lower()
    count += 1
    if 'n' == c:
        break
print(f'A lista tem {count} elementos')
print(valores[::-1])
if 5 in valores:
    print('O valor 5 faz parte da lista')
if 5 not in valores:
    print('O valor 5 não faz parte da lista')