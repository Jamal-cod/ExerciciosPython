from random import randint
from time import sleep

print('Olá, vamos jogar jokenpo')
print('''[1] PEDRA 
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('COmputador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogador]))
if computador == 0:
      if jogador == 0:
            print('EMPATE \nTente novamente')
      elif jogador == 1:
            print('Computador VENCEU')
      elif jogador == 2:
            print('Jogador VENCEU')
if computador == 1:
      if jogador == 0:
            print('Jogador VENCEU')
      elif jogador == 1:
            print('EMPATE'
                  '\n Tente novamente')
      elif jogador == 2:
            print('Computador venceu')
if computador == 2:
      if jogador == 0:
            print('Computador venceu')
      elif jogador == 1:
            print('Jogador venceu')
      elif jogador == 2:
            print('''EMPATE
            Tente novamente''')