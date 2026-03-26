from operator import itemgetter
from random import randint
from time import sleep

jogo = {'Danilo': randint(1, 6),
        'Maria': randint(1, 6),
        'Gael': randint(1, 6),
        'Alice': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, l in enumerate(ranking):
    valor = l[0]
    valor2 = l[1]
    posicao = ranking.index(l)+1
    print(f'Em {posicao}°lugar {valor} com o numero {valor2}')
    sleep(1)
print()
print('\t\tJOGANDO NOVAMENTE')
print()
sleep(0.5)
from operator import itemgetter
from random import randint
from time import sleep

jogo = {'Danilo': randint(1, 6),
        'Maria': randint(1, 6),
        'Gael': randint(1, 6),
        'Alice': randint(1, 6)}
ranking = dict()
print('\tValores sorteados:')
for k, v in jogo.items():
    print(f'  {k} tirou o numero {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\t==== RANKING ====')
sleep(0.8)
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar {v[0]} com {v[1]}')
    sleep(1)