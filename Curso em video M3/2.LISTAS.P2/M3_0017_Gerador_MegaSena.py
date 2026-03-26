from random import randint
from time import sleep

lista = []
jogos = []
print('-' * 30)
print('JOGA NA MEGA SENA'.center(30))
print('-' * 30)
quant = int(input('Quantos valores deseja gerar: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    sleep(0.8)
    print(f'Jogo {i + 1}: {l}')
print('-=' * 5, 'Boa Sorte', '-=' * 5)
print(f'O valor é de R$: {quant * 3:.2f}')