import random
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 6 valores: ', end='')
    for cont in range(0,6):
        n = (randint(1,10))
        lista.append(n)
        print(f'{n}', end=',', flush=True)
        sleep(0.3)
    print('fim')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')
    sleep(0.3)


numero = list()
sorteia(numero)
somapar(numero)