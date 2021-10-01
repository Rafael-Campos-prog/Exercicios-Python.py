num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
       num.append(n)
       print('Valor adicionado com sucesso!')
    else:
       print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
num.sort()
print(f'Você digitou os valores{num}')
