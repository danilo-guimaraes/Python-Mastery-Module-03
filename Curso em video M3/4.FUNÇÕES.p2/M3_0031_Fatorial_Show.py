from random import randint


def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


aleat = randint(4, 10)
print(fatorial(aleat, True))
print(fatorial(aleat, False))
print('O numero da soma fatoria fico = {}'.format(fatorial(aleat)))
num = int(input('Escolha um numero: '))
print(fatorial(num, True))