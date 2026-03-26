aprovacao = {}
nome = str(input('Qual nome do Aluno: ').capitalize())
aprovacao['nome'] = nome
media = float(input(f'Qual a media de {nome}? '))
aprovacao['media'] = media
print()
if aprovacao['media'] >= 7:
    aprovacao['aprovação'] = 'Aprovado'
    print(f'O aluno {nome} foi aprovado, com a media de {aprovacao["media"]}.')
elif 7 > aprovacao['media'] >= 5:
    aprovacao['recuperação'] = 'Recuperação'
    print(f'O aluno {nome} esta de recuperacao com a media de {aprovacao["media"]}.')
else:
    aprovacao['aprovação'] = 'Reprovado'
    print(f'O aluno {nome} foi reprovado com a media de {aprovacao["media"]}.')
print()
print(aprovacao.items())