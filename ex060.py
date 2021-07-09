from math import factorial
c = int(input('Digite um valor para saber o seu fatorial: '))
n = c
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    c -= 1
    if c > 0:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(factorial(n), end='')


