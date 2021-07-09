def ficha(jog, gols):
    print(f'O {jog} fez {gols} gol(s) no campenoato')

jog = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    if gols.strip() == '':
        gols = 0
if jog.strip() == '':
    jog = '<Desconhecido>'
ficha(jog, gols)