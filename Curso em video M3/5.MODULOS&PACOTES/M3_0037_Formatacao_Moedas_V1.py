from MODULOS.uteis import moedas

valor = int(input('Digite um valor: R$'))
print(f'A metade do valor de R$:{valor} é {moedas.moedas(moedas.metade(valor))}')
print(f'O dobro do valor de R$:{valor} é {moedas.moedas(moedas.dobro(valor))}')
print(f'Aumentando 10%, temos {moedas.moedas(moedas.aumentar(valor, 10))}')
print(f'Diminuindo 13%, temos {moedas.moedas(moedas.diminuir(valor, 13))}')