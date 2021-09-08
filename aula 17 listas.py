num = [2, 5, 2, 9, 1]
num[2] = 3
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 5)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
