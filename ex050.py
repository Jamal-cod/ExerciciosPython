s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont += 1
        s += n
print('Você informou {} números pares e a soma foi {}'.format(cont, s))