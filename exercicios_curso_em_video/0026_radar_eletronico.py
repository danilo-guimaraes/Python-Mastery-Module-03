velocidade = float(input('Digite uma velocidade: ').strip(' '))
if velocidade > 80:
 multa = (velocidade - 80) * 7
 print('Voce foi multado em R$:{:.2f}'.format(multa))
else:
 print('Voce esta abaixo do limite de velocidade, continue assim')