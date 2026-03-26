from time import sleep

from MODULOS.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Sair do Programa, até logo...')
        break
    else:
        cabeçalho('\033[31mERRO! DIGITE UMA OPÇÃO VALIDA!\033[m')
    sleep(1)