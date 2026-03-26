from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m',
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(1)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP V3.0035', 5)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('FIM DO PROGRAMA', 1)
