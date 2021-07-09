def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: Uma ou mais notas de vários alunos.
    :param sit:valor opcional, indicando se deve ou não adcionar a avaliação.
    :return:dicionário com várias informações sobre a situação dos alunos.
    """
    alunos = {}
    alunos['Quantidade de notas'] = len(n)
    alunos['Maior nota'] = max(n)
    alunos['Menor nota'] = min(n)
    alunos['Média'] = sum(n)/len(n)
    if sit == True:
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'Boa'
        elif alunos['Média'] >= 5 and alunos['Média'] < 7:
            alunos['Situação'] = 'Razóavel'
        else:
            alunos['Média'] = 'Ruim'
    print(alunos)
help(notas)