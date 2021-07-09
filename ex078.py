lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c+1}: ')))
print('-=' * 20)
print(f'Você digitou os valores {lista}')
max = max(lista)
min = min(lista)
print(f'O maior valor digitiado foi {max} na posição {lista.index(max)+1}')
print(f'O maior número está na {lista.index(max)+1}° posição')
print(f'O maior valor digitado foi {min} na posição {lista.index(min)+1}')
print(f'O menor valor está na {lista.index(min)+1}° posição')