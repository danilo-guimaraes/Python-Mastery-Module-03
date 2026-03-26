from time import sleep
from datetime import date

cadastro = {}
nome = str(input('Qual nome do Aluno: ').capitalize())
cadastro['Nome'] = nome
ano = int(input('Qual o Ano do nascimento: '))
cadastro['Ano'] = ano
carteira = int(input('Qual numero do carteira de trabalho: (0 nao tem) '))
cadastro['Carteira'] = carteira
idade = date.today().year - ano
if cadastro['Carteira'] > 0:
    contratacao = int(input('Ano de Contratação: '))
    cadastro['Contratação'] = contratacao
    salario = float(input('Salário: '))
    cadastro['Salário'] = salario
    aposentadoria = 65 - (date.today().year - contratacao)
    print('Nome: ', cadastro['Nome'])
    print(f'Idade: {idade}')
    print('Ano: ', cadastro['Ano'])
    print('Carteira: ', cadastro['Carteira'])
    print('Ano de contratação: ', cadastro['Contratação'])
    print('Salário: R$',cadastro['Salário'])
    print(f'Se aposentara com {aposentadoria} anos')
else:
    print('Nome: ', cadastro['Nome'])
    print(f'Idade: {idade}')
    print('Carteira: Nao possui carteira')
    print('Voce nao pode trabalhar sem carteira')
