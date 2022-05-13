def notas(*num, sit=False):
    """[Função para analisar notas e situações de vários alunos]

    Args:
        sit (bool, optional): [valor opcional, indicando se deve ou não adicionar a situação]. Defaults to False.

    Returns:
        [type]: [dicionário com várias informações sobre a situação da turma]
    """
    boletim = {}
    boletim['total'] = len(num)
    for i, valor in enumerate(num): # é possivel descobrir o maior e menor valor apenas usando funções max() e min() para agilizar.
        if i == 0:
            boletim['maior'] = valor
            boletim['menor'] = valor
        else:
            if valor > boletim['maior']:
                boletim['maior'] = valor
            else:
                if valor < boletim['menor']:
                    boletim['menor'] = valor
    boletim['média'] = sum(num) / len(num)
    if sit == True:
        if boletim['média'] < 6:
            boletim['situação'] = 'RUIM'
        elif boletim['média'] > 7:
            boletim['situação'] = 'BOA'
        else:
            boletim['situação'] = 'RAZOÁVEL'
    return boletim


resp = notas(2, 3.5, 4.4, 2, 6.8, sit=True)
print(resp)
