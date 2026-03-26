valores = []
par = []
impar = []

while True:
    v = int(input('Digite um valor: '))
    valores.append(v)

    while True: 
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('OPÇÃO INVÁLIDA! ', end='')
    if resp == 'N':
        break


for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
