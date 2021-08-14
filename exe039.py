from datetime import date
atual = date.today().year
nasc = int(input('\033[36mAno de nascimento:\033[m'))
idade = atual - nasc
print('\033[34mQuem nasceu em {} tem {} anos em {}.\033[m'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('\033[33mAinda faltam {} anos para o alistamento\033[m'.format(saldo))
    ano = atual + saldo
    print('\033[33mSeu alistamento será em {}.\033[m'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('\033[31mVocê já deveria ter se alistado há {} anos.\033[m'.format(saldo))
    ano = atual - saldo
    print('\033[33mSeu alistamento foi em {}.\033[m'.format(ano))

