n = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
bc = int(input('Sua escolha: '))
if bc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif bc == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif bc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))