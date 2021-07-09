frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
invertido = frase[:: -1]
if frase == invertido:
    print('A frase {} é um palíndromo: {}'.format(frase, invertido))
else:
    print('A frase {} não é um palíndromo'.format(frase))