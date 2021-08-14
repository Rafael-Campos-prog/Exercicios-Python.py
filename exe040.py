n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, média))
if média >= 5 and média < 7:
    print('Então o aluno está em\033[33m RECUPERAÇÃO!\033[m')
elif média < 5:
    print('O aluno está\033[31m REPROVADO!\033[m')
elif média >= 7:
    print('O aluno está\033[34m APROVADO!\033[m')