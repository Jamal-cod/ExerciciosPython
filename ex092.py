from datetime import datetime
n = datetime.now()
pessoa = dict()
pessoa['Nome'] = str(input('Nome: ')).capitalize()
pessoa['Ano de nascimento'] = int(input('Ano de nascimento: '))
pessoa['Idade'] = n.year - pessoa['Ano de nascimento']
pessoa['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['Ctps'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Ano de contratação'] + 35 - pessoa['Ano de nascimento']
print('-' * 20)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')