s = 0
velho = 0
idade = 0
velho = 0
nomevelho = ''
cont = 0
for c in range(1, 5):
    print('------ {} Pessoa ------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    s += idade
    if c == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    elif sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    if idade < 20 and sexo == 'F':
        cont += 1


print('A média das idades do grupo é {}'.format(s / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
