nome = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
a = nome.split()
print('Seu primeiro nome é {}'.format(a[0]))
a.reverse()
print('Seu último nome é {}'.format(a[0]))