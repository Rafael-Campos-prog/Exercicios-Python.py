soma = 0
cont = 0
for tri in range(1, 501, 2):
    if tri % 3 == 0:
         cont = cont + 1
         soma = soma + tri
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))


