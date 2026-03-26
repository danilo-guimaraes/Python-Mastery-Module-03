palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    # Ajeitado: Mostra a palavra primeiro (em maiúsculas fica mais profissional)
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')

    for letra in palavra:
        if letra.lower() in 'aeiou':
            # Ajeitado: Dá um espaço entre as vogais para não grudarem
            print(f'{letra} ', end='')
