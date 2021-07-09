sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
while sexo not in 'mMFf':
    sexo = str(input('Dados inválidos! Por favor, informe o seu sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado'.format(sexo))