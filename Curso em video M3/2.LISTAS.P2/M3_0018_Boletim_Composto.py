ficha = []
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 5, 'FIM DO PROGRAMA', '-=' * 5)
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
print('-' * 26)
for i, l in enumerate(ficha):
    print(f'{i+1:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    print('-' * 40)
    opc = int(input('Mostra a nota de qual aluno? (999 pra sair): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Nota do aluno {ficha[opc][0]} sao {ficha[opc][1]}')
print('FIM DO PROGRAMA')