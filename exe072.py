contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
opc = ' '
while True:
    n = int(input(f'Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
            break
    print('Tente novamente!', end='')
print(f'Você digitou o número {contagem[n]}')

