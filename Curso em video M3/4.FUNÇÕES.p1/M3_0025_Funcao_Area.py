def area(l, c):
    print('-=' * 30)
    s = l * c
    print(f'A soma da largura {l} x {c} de comprimento é de {s}m² ')
    print('-=' * 30)


largura = float(input('digite a largura: '))
comprimento = float(input('digite a comprimento: '))
area(largura, comprimento)
