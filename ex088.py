from random import randint
from time import sleep
lista = list()
print('-------------------------')
print("     JOGA MEGA SENA     ")
print('-------------------------')
game = int(input('Quantos jogos quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {game} JOGOS -=-=-=')
for c in range(0, 6):
    lista.append(randint(0, 60))
for c in range(0, game):
    lista.sort()
    print(f'jogo {c+1}: {lista}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')