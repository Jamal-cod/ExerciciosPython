valores = []
par = []
impar = []
while True:
    i = (int(input('Digite um número: ')))
    if i % 2 == 0:
        par.append(i)
    if i % 2 != 0:
        impar.append(i)
    valores.append(i)
    c = str(input('Quer continuar [S/N]? ')).upper()
    if 'N' in c:
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')