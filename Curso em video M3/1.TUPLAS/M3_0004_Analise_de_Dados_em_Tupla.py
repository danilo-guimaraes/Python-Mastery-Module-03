tupla = (int(input('Primeiro valor: ')),
         int(input('Segundo valor: ')),
         int(input('Terceiro valor: ')),
         int(input('Quarto valor: ')))

# Ajeitado: Organização da Saída
print(f'Você digitou os valores {tupla}')

# 1. Contagem do 9
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')

# 2. Posição do 3
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

# 3. Números Pares
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')