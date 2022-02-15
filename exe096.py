def área(larg, comp):
    a = larg * comp
    print(f' A área de um terreno {larg} X {comp} é de {a}m².')


# Programa principal
print('Calcule a Área de um terreno.')
print('>' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
