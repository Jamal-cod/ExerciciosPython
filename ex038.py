a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('{} é maior que {}'.format(a, b))
elif b < a:
    print('{} é maior que {}'.format(b, a))
elif a == b:
    print('Os dois valores são IGUAIS')