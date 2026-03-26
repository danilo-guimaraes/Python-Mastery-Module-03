valores = list()
n = 5
while True:
    v = int(input('Digite um valor: '))

    if v not in valores:
        valores.append(v)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if v == 5:
            n = valores.index(v)
            print('O valor 5 faz parte da lista')
        if resp in 'SN':
            break
        print('OPÇÃO INVÁLIDA! ', end='')

    if resp == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')
