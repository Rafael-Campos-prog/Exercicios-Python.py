from time import sleep
soma = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar):'))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
sleep(1)
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
sleep(2)
print('Fim do programa. Você digitou 999.')
sleep(2)
print('Obrigado pela preferência.Volte sempre!')

