from random import randint
from time import sleep
números = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in números:
    sleep(1)
    print(f'{n} ', end='')
sleep(2)
print(f'\nO maior valor sorteado foi {max(números)}')
sleep(2)
print(f'O menor valor sorteado foi {min(números)}')
