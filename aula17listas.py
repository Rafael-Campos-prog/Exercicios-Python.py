num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não tem o número 4 em sua lista!')
print(num)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

'''values = list()
for cont in range(0, 5):
    values.append(int(input('Digite um valor: ')))
for c,v in enumerate(values):
    print(f'Na posição {c} encontrei o valor {v}!')'''
# O python cria uma ligação entre uma lista e outra, como no exemplo abaixo.
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Para criar uma cópia de uma lista:
print('_-'*30)
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
