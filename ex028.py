from random import randint
print('Tente adivinhar o número entre 0 e 5 que eu pensei')
r = int(input('Qual o seu palpite? '))
t = randint(1, 5)
if r == t:
    print('Parabéns você me venceu')
else:
    print('O computador venceu')
print('----FIM----')
