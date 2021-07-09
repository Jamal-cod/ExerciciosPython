s = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        s = s + c
print('A soma de todos valores solicitados é {}'.format(s))