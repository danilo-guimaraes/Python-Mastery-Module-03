try:                                                                              # Inicia o bloco de teste para capturar possíveis erros
    numero = str(input('Vamos ver se seu numero é par ou impar, escolha um numero: ')) # Lê a entrada do usuário como string (texto)
    numero = int(numero)                                                          # Tenta converter o texto para número inteiro (onde pode dar erro)
    if numero % 2 == 0:                                                           # SE o resto da divisão por 2 for zero (lógica de par)
        print('Seu numero é par')                                                 # Executa se a condição de par for verdadeira
    else:                                                                         # SENÃO (se houver resto na divisão)
        print('Seu numero é impar')                                               # Executa se o número for ímpar
except ValueError:                                                                # Se o usuário digitar letras, o Python gera um 'ValueError'
    print('Voce errou, tente novamente')                                          # Captura o erro e exibe essa mensagem em vez de travar o script
