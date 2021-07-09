from random import randint
rand = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
ordem = sorted(rand)
print(f'Os valores sorteados foram {rand}')
print(f'O menor valor sorteado foi {ordem[0]}')
print(f'O maior valor sorteado foi {ordem[-1]}')