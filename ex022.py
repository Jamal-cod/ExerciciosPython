nome = str(input('Olá, qual o seu nome completo? ')).strip()
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
dividido = nome.split()
junto = ''.join(dividido)
print('O seu nome tem {} caracteres'.format(len(junto)))
n1 = (dividido[0])
print('Seu primeiro nome tem {} carecteres'.format(len(n1)))



