ext = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
       'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dessezeis', 'Dessezete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 1 e 20: '))
    if num > 0 and num < 21:
        print(f'Você digitou {ext[num-1]}')
        break