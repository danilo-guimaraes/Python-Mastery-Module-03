

brasileirao = ('São Paulo', 'Palmeiras', 'Fluminense', 'Bahia', 'Flamengo', 'Coritiba', 'Gremio',
               'Corinthians', 'Bragantino', 'Atletico-PR', 'Vitoria', 'Chapecoense', 'Mirasol',
               'Santos', 'Vasco', 'Atletico-MG', 'Botafogo', 'Remo', 'Cruzeiro', 'Internacional')


top5 = brasileirao[:5]
rebaixar = brasileirao[-4:]
ordem = sorted(brasileirao)

chape = brasileirao.index('Chapecoense') + 1

print(f'Os 5 primeiros são: {top5}')
print('-' * 30)
print(f'Os 4 últimos (Z4) são: {rebaixar}')
print('-' * 30)
print(f'Times em ordem alfabética: \n{ordem}')
print('-' * 30)
print(f'A Chapecoense está na {chape}ª posição.')
