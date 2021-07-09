pp = dict()
l = list()
sumt = 0
while True:
    pp['nome'] = str(input('Nome: '))
    pp['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    pp['idade'] = int(input('Idade: '))
    resp = str(input('Quer continuar [S/N]? ')).upper()[0]
    l.append(pp.copy())
    if resp == 'N':
        break
print('-=' * 20)
for c in range(0, len(l)):
    sumt += pp['idade']
    media = sumt / len(l)
print(f'- A média de idade é de {media}')
print(f'- O total de {len(l)} pessoas foram cadastradas')
if pp['sexo'] == 'F':
    print(f'- As mulheres cadastradas foram: {pp["nome"]}')
print('- Lista de pessoas que estão acima de média: ')
if pp['idade'] >= media:
    print(pp['nome'])
else:
    print('Sem mais pessoas com idade acima da média')