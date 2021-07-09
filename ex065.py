i = 'SsNn'
soma = maior = menor = c = cont = 0
while i not in 'Nn':
    c = int(input('Digite um número: '))
    i = input('Quer continuar [S/N]? ').upper()
    cont += 1
    soma += c / cont
    if cont == 1:
        maior = menor = c
    else:
        if c > maior:
             maior = c
        if c < menor:
             menor = c
print('Você digitou {} números e a média foi {:.2f}'.format(cont, soma))
print('O maior número digitado foi {} e o menor {}'.format(maior, menor))