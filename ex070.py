print('          LOJAS JAMAL         ')
print("=" * 20)
total = 0
cont = 1
cont2 = 0
menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    n = str(input('Quer continuar [S/N]? ')).upper()
    print('-' * 15)
    total += preço
    if preço > 1000:
        cont2 += 1
    if cont == 1 :
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    if n == 'N':
        break
print(f'Total da compra: {total}')
print(f'Quantos produtos que custam mais de R$1000: {cont}')
print(f'O produto {barato} é o mais barato e custa {menor}')
