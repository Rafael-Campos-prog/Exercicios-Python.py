soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor:'.format(c)))
    if num % 2 == 0:    # se o número digitado for par, dividir por dois e verificar se a divisão é igual a zero.
        soma = soma + num # idetação = só vai somar  e contar se os números forem pares.
        cont = cont +1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))