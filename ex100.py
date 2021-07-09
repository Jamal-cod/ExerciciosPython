from random import randint
from time import sleep
 # Adicionar os sorteados a uma lista
numeros = []

 # Criar Duas funções
 #Sortear 5 números e guardar na lista
def sorteio():
    for c in range(0, 5):
        i = (randint(0, 6))
        numeros.append(i)
    print('Sorteando 6 valores da lista: ', end='')
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.5)
 #Somar os números pares da lista
def somapar():
    sum = 0
    for n in numeros:
        if n % 2 == 0:
            sum += n
    print(f'\nSomando os valores pares de {numeros}, temos {sum} ')

sorteio()
somapar()