galera = list()
dados = dict()
soma = media = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ').capitalize())

    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    galera.append(dados.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media da soma das idades e de {media:5.2f} anos.')
print(f'C) As mulhers cadastradas foram: ', end='')

for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"].capitalize()}, ', end='')
print()
print(f'D) Lista das pessoas que estao acima da media: ')

for p in galera:
    if p['Idade'] >= media:
        print(f'   ', end='')
        for k, v in p.items():
            print(f' {k} = {v};', end='')
    print()
print('<<ENCERRADO>>')