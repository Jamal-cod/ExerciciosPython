from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1, 7),
         'Jogador 2': randint(1, 7),
         'Jogador 3': randint(1, 7),
         'Jogador 4': randint(1, 7)}
ranking = list()
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'    O {k} tirou {v}')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('Ranking')
for k, v in enumerate(ranking):
    print(f'    {k+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)