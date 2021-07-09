tabela = ('Bragantino', 'Bahia', 'Ceará', 'Fortaleza',
          'Atlético-PR', 'Flamengo', 'Atlético-GO',
          'Sport recife', 'Juventude', 'Cuiába',
          'Internacional', 'São Paulo', 'Fluminense',
          'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras',
          'Corinthians', 'Chapecoense', 'Santos')
print('-' * 40)
print(f'Lista de times do Brasileirão {tabela}')
print('-' * 40)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-' * 40)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-' * 40)
print(f'Em ordem alfabética: {sorted(tabela)}')
print('-' * 40)
print(f'O chapecoense está na {tabela.index("Chapecoense")+1}° posição')
