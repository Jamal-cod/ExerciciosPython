valores = []
for c in range(0, 5):
    i = (int(input('Digite um número: ')))
    if c == 0 or i > valores[-1]:
        valores.append(i)
    else:
        pos = 0
        while pos < len(valores):
            if i <= valores[pos]:
                valores.insert(pos, i)
                break
            pos += 1
print(valores)