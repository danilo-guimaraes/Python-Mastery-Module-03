from time import sleep
from MODULOS.arquivo import *
from MODULOS.interface import *

arq = 'curso.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Sair do Programa, até logo...')
        break
    else:
        cabeçalho('\033[31mERRO! DIGITE UMA OPÇÃO VALIDA!\033[m')
    sleep(1)
