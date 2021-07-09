c = cont = s = 0
while True:
    c = int(input('Digite um número [99 pra parar]: '))
    if c == 999:
        break
    cont += 1
    s += c
print(f'A soma dos {cont} valores é igual a {s}')