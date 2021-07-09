from time import sleep
def ajuda():
    while True:
        tam = len('SISTEMA DE AJUDA PYHELP') + 4
        print('-' * tam)
        print('  \033[036mSISTEMA DE AJUDA PYHELP\033[m')
        print('-' * tam)
        val = str(input('Função ou Biblioteca -> ')).strip()
        sleep(1)
        tam2 = len(f'Acessando o manual do comando {val}') + 4
        print('-' * tam2)
        print(f'  \033[33mAcessando o manual do comando {val}\033[m')
        print('-' * tam2)
        sleep(1)
        help(val)
        if val == 'fim':
            break

ajuda()