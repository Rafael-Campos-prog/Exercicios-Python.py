#Interactive Help e docstrings


def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada pelo Gustavo Guanabara do Curso em Vídeo.
    """
    c = i
    while c <= f :
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)

contador(0, 100, 10)
