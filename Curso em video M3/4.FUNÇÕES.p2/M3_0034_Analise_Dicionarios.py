from random import randint


def notas(*n, sit=False):
    """-> Função para analisar as notas de varios alunos
        :param n: uma ou mais notas dos alunos.
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionario com varias informações sobre a situação da turma"""

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['Situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['Situacao'] = 'Razoavel'
        else:
            r['Situacao'] = 'Ruim'
    print(f'O total foi {r["total"]}, com a maior sendo {r["maior"]} e o menor {r["menor"]}\n'
          f'e a media foi {r["media"]}, situacao: {r["Situacao"]}')
    return r

resp = notas(randint(0, 10), randint(0, 10), randint(0, 10), sit=True)

