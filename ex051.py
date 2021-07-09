c = int(input('Primeiro termo da progressão: '))
r = int(input('Razão: '))
u = c + (10) * r
for c in range(c, u, r):
    print(c, end=' . ')