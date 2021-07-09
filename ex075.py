a = int(input('Digite um valor: '))
b = int(input('Digite outro: '))
c = int(input('Digite mais um: '))
d = int(input('Digite o último: '))
valores = (a, b, c, d)
print('Você digitou os valores {}'.format(valores))
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}° posição')
if 3 not in valores:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')