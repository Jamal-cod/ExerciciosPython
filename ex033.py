n = int(input('Primeiro valor: '))
n1 = int(input('Segundo valor: '))
n2 = int(input('Terceiro valor: '))
menor = n
if n1 < n2 and n1 < n:
    menor = n1
if n2 < n1 and n1 < n:
    menor = n2
maior = n
if n1 > n2 and n1 > n:
    maior = n1
if n2 > n1 and n2 > n:
    maior = n2
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))