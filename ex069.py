print('Cadastre a pessoa')
print('-' * 20)
age = cont = 0
cont1 = 0
cont2 = 0
sex = 'MmFf'
while True:
    age = int(input('Qual a idade? '))
    sex = str(input('Qual o sexo [M/F]? ')).upper().strip()
    print('-' * 20)
    i = str(input('Quer continuar [S/N]? ')).upper().strip()
    print('-' * 20)
    if age > 18:
        cont += 1
    if sex in 'Mm':
        cont1 += 1
    if sex in 'Ff' and age < 20:
        cont2 += 1
    if i in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}'
      f'\nAo todo temos {cont1} homens cadastrados'
      f'\nE temos {cont2} mulheres com menos de 20 anos')