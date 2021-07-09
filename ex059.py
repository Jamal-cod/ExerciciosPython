
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
action = 0
while action != (5):
    print('[1]Somar '
      '\n[2]Multiplicar'
      '\n[3]Maior'
      '\n[4]Novos números'
      '\n[5]Sair do programa')
    action = int(input('O que você deseja fazer? '))
    if action == 1:
        s = n1 + n2
        print('A soma entre os valores {} e {} é igual a {}'.format(n1, n2, s))
        print('=' * 20)
    elif action == 2:
        m = n1 * n2
        print('O produto de {} e {} é {}'.format(n1, n2, m))
        print('=' * 20)
    elif action == 3:
        lista = [n1, n2]
        print('O maior valor entre {} e {} é {}'.format(n1, n2, max(lista)))
        if n1 == n2:
            print('Os dois valores são iguais')
        print('=' * 20)
    elif action == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('=' * 20)
    elif action == 5:
        print('Ok')
print('Programa desligado')
print('=' * 20)

