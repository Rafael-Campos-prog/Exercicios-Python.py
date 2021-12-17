teste = list()
teste.append('Rafael')
teste.append(38)
galera = list()
galera.append(teste[:])
teste[0] = 'Joceane'
teste[1] = 41
galera.append(teste[:])
print(galera)

funcionários = ['Rafael', 38], ['Joceane', 41], ['Isabela', 10], ['Adailto', 73]
#print(funcionários[2] [1])
for p in funcionários:
    print(f'{p[1]}')
