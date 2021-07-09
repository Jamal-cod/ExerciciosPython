pessoas = []
dados = []
max = min = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(dados) == 0:
        max = min = pessoas[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar [S/N]? ')).upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{len(pessoas)} foram cadastradas')
for p in pessoas:
    if p[1] == max:
        print(f'{max}kg, o maior peso de, {p[0]}')
for p in pessoas:
    if p[1] == min:
        print(f'{min}kg, O menor peso de, {p[0]}')