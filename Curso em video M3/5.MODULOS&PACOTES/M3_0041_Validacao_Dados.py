from MODULOS.uteis import moedas
from MODULOS.dados import leiadinheiro

p = leiadinheiro('Digite um valor: R$')
a = leiadinheiro('Digite quantos % de aumento: ')
d = leiadinheiro('Digite quantos % de redução: ')
moedas.resumo(p, a, d)