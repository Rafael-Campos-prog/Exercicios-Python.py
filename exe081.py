num = list()
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
num.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram {num}')
print(f'Foram digitados {len(num)} números.')
if 5 in num:
    print('O número 5 foi digitado e está nesta lista.')
else:
    print('O número 5 não faz parte desta lista.')
