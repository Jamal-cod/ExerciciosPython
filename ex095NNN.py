jogadores = dict()
pontos = []
time = list()
print('-' * 25)
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        pontos.append(gols)
        jogadores['gols'] = pontos
        jogadores['total'] = sum(pontos)
        time.append(jogadores.copy())
    resp = str(input('Quer continuar [S/N]? ')).upper()[0]
    if resp == 'N':
        break
print(time)
