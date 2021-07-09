
def voto(ano):
    from datetime import datetime
    agr = datetime.now().year
    idade = agr - ano
    if idade < 16:
        print(f'Com {agr-ano} anos: NÃO VOTA')
    if idade < 65 and idade >= 18:
        print(f'Com {agr-ano} anos: VOTO OBRIGATÓRIO')
    if idade > 65:
        print(f'Com {agr-ano} anos: VOTO OPCIONAL')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)