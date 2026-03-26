from time import sleep

from MODULOS.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileNotFoundError:
        print('Aconteceu um erro ao ler o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Aconteceu um erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'Nome: {dados[0]}, Idade: {dados[1]}')
            sleep(0.6)

    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao ler o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao ler o arquivo.')
        else:
            print(f'Novo registro do nome \033[31m{nome.capitalize()}\033[m, de idade {idade} anos com sucesso!')
            a.close()
