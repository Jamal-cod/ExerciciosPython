jogador = dict()
pontos = list()
cont = 0
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
for v in jogador.values():
    plays = int(input(f'Quantas partidas {v} jogou? '))
for c in range(0, plays):
    gols = int(input(f'Quantos gols na partida {c + 1}? '))
    pontos.append(gols)
    jogador['gols'] = pontos
    cont += gols
    jogador['total'] = cont
print('-=' * 25)
print(jogador)
print('-=' * 25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {plays} partidas')
for k, v in enumerate(pontos):
    print(f'=> Na partida {k+1}, fez {v} gols.')