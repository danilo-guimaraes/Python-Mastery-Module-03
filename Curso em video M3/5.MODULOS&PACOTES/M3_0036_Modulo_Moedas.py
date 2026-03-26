from MODULOS.uteis import moedas

valor = int(input('Digite um valor: '))
print(f'A metade do valor de R$:{valor:.1f} é R$:{moedas.metade(valor):.1f}')
print(f'O dobro do valor de R$:{valor:.1f} é R$:{moedas.dobro(valor):.1f}')
print(f'Aumentando 10%, temos R$:{moedas.aumentar(valor, 10):.1f}')
print(f'Diminuindo 13%, temos R$:{moedas.diminuir(valor, 13):.1f}')
