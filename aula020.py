from time import sleep


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


# Programa principal
mensagem('      Rafael Campos ')
sleep(1)
mensagem('      Curso de Python')
sleep(1)
mensagem('    Aprendendo Funções')
sleep(1)


def soma(a, b):
    s = a + b
    print(s)


# Programa principal
soma(4, 1)
sleep(1)
soma(5, 3)
sleep(1)
soma(2, 7)


def contador(*num):
    for valor in num:
        print(f' {valor} ', end=' ')


#programa principal
contador(2, 1, 3)
contador(4, 3, 6, 8, 1,)