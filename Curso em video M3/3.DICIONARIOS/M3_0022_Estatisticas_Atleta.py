from random import randint

jogador = {}
total_gols = []
nome = str(input('Qual nome do jogador: ').capitalize())
jogador['Nome: '] = nome
for g in range(0,5):
    gols = (randint(0,3))
    total_gols.append(gols)
    jogador['Gols: '] = total_gols
    jogador['Total: '] = sum(total_gols)
print('-'*30)
print(jogador)
print('-'*30)
for k, v in jogador.items():
    print(f'{k} {v}')
print('-='*30)
partidas = len(total_gols)
print(f'O jogador {nome} jogou {partidas} partidas.')
for g in range(0,5):
    print(f'=> Na partida {g+1} fez {total_gols[g]}! ')
print(f'Foi um total de {sum(total_gols)} gols.')