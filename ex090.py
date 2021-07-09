escola = {}
escola['Nome'] = str(input('Aluno(a): ')).capitalize()
escola['Média']= float(input(f'Média de {escola["Nome"]}: '))
if escola['Média'] < 7:
    escola['Situação'] = 'REPROVADO'
else:
    escola['Situação'] = 'APROVADO'
for k, v in escola.items():
    print(f'{k} é igual a {v}')