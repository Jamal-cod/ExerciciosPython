matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
sump = sumc = maxl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a posição {l, c} da matriz: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]}  ]', end='')
        if matriz[l][c] % 2 == 0:
            sump += matriz[l][c]
    print()
print('-=' * 20)
for l in range(0, 3):
    sumc += matriz[l][2]
for c in range(0, 3):
    if matriz[1][c] == 1:
        maxl = 1
    else:
        if matriz[1][c] > maxl:
            maxl = matriz[1][c]
print(f'A soma de todos os valores pares é igual a {sump}')
print(f'A soma de todos os valores da terceira colunda é igual a {sumc}')
print(f'O maior valor da segunda linha é o {maxl}')