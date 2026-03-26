from MODULOS.uteis import moedas

valor = int(input('Digite um valor: R$'))
print(f'A metade do valor de R$:{valor} é {moedas.metade(valor, True)}')
print(f'A metade do valor de R$:{valor} é {moedas.metade(valor, False)} = parametro Falso')
print(f'O dobro do valor de R$:{valor} é {moedas.dobro(valor, True)}')
print(f'O dobro do valor de R$:{valor} é {moedas.dobro(valor, False)} = parametro Falso')
print(f'Aumentando 10%, temos {moedas.aumentar(valor, 10, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(valor, 10, False)} = parametro Falso')
print(f'Diminuindo 13%, temos {moedas.diminuir(valor, 13, True)}')
print(f'Diminuindo 13%, temos {moedas.diminuir(valor, 13, False)} = parametro Falso')
