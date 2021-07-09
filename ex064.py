c = 0
soma = 0
cont = 0
while c != 999:
    c = int(input('Digite um número[999 pra parar]:'))
    soma += c
    cont += 1
print('Você digitou {} números e a soma entre eles é {}'.format(cont - 1, soma - 999))