listagem = ('Pao', 3, 'Leite', 5.50, 'Lapis', 2.50,
            'Borracha', 0.50, 'Estojo', 5.80)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(len(listagem)):
    if pos % 2 == 0:

        print(f'{listagem[pos]:.<30}', end='')
    else:

        print(f'R${listagem[pos]:>7.2f}')

print('-' * 40)