def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
        except:
            print('\033[031mERRO! Digite um número válido, por favor\033[m')
        else:
            print(f'O valor digitado foi {n}')


def leiafloat():

    try:
        n1 = float(input('Digite um número real: '))
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os dados!')
    except:
        print('\033[031mERRO! Digite um número válido por favor')
    else:
        print(f'O valor digitado foi {n1}')


leiaint()
leiafloat()
