def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            resp = str(input('Voce quer continuar? [S/N] ')).strip().upper()[0]
            if resp in 'Nn':
                break
    return valor


n = leiaInt("Digite um numero inteiro: ")
print(f'Voce acabou de digitar o numero {n}')
