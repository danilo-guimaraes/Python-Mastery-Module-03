from time import sleep


def aumentar(valor=0, taxa=0, resposta=False):
    res = valor + (valor * taxa / 100)
    return res if resposta is False else moedas(res)

def diminuir(valor=0, taxa=0, resposta=False):
    res = valor - (valor * taxa / 100)
    return res if resposta is False else moedas(res)

def dobro(valor=0, resposta=False):
    res = valor * 2
    return res if not resposta else moedas(res)

def metade(valor=0, resposta=False):
    res = valor / 2
    return res if not resposta else moedas(res)

def moedas(valor=0, moedas='R$'):
    sleep(1)
    return f'{moedas}{valor:.2f}'.replace('.', ',')

def resumo(valor, aum, dim):
    print(f'-'*40)
    print(f'Resumo do valor'.center(40))
    print(f'-'*40)
    print(f'Resumo do valor: {moedas(valor)}')
    aumento = valor + (valor * aum / 100)
    reducao = valor - (valor * dim / 100)
    dobro = valor * 2
    metade = valor / 2
    print(f'Dobro do valor:   {moedas(dobro)}')
    print(f'Metade do valor:  {moedas(metade)}')
    print(f'{aum}% de aumento:  {moedas(aumento)}')
    print(f'{dim}% de redução:  {moedas(reducao)}')
    print(f'-'*40)
