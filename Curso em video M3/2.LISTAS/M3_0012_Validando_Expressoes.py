expressao  = str(input('Digite a expressao: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')