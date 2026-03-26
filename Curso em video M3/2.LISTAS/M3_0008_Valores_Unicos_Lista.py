valores = list()
while True:
    v = int(input('Digite um valor: '))

    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')


    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('OPÇÃO INVÁLIDA! ', end='')

    if resp == 'N':
        break

print('-=' * 30)
valores.sort()
print(f'Você digitou os valores: {valores}')
print('-=' * 30)
print(f' a soma dos valores em uma lista: {sum(valores)}')