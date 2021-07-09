v = int(input('Qual a velocidade atual do carro? '))
if v > 80:
    m = 7 * (v - 80)
    print('MULTADO! você excedeu o limite de 80km/h'
          '\nVocê deve pagar uma multa de R${}.'.format(m))
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('Tenha um bom dia! Dirija com segurança.')