from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f"Com a idade de {idade}, Voce nao pode votar")
    elif idade > 16 and idade < 18:
        print(f"Com a idade de {idade}, Voto opcional")
    elif idade >= 18 and idade <= 65:
        print(f"Com a idade de {idade}, Voto obrigatorio")
    else:
        print(f"Com a idade de {idade}, Voto opcional")


ano = int(input("Digite se ano de nascimento: "))
voto(ano)
