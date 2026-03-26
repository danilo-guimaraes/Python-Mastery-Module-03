def ficha(nome='<desconhecido>', gols=0):
    print(f" {nome} fez {gols} Gol(s)")

nom = str(input("Qual o nome do jogador? ")).capitalize()
gol = str(input('Quantos gols na partida? '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nom.strip() == '':
    ficha(gols=gol)
else:
    ficha(nom, gol)

