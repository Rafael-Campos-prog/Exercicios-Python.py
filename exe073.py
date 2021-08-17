times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino',
         'Flamengo', 'Athletico-PR', 'Atlético-GO', 'Ceará', 'Internacional',
         'Santos', 'Corinthians', 'Juventude', 'Bahia', 'São Paulo', 'Fluminense',
         'Cuiabá', 'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')
print('=-'*35)
#print(f'Lista de times: {times}')
#for t in times:
 #   print(t)
print(f'Lista do Brasileirão: {times}')
print('=-'*35)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('=-'*35)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('=-'*35)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*35)
print(f' O Chapecoense está na {times.index("Chapecoense")+1}ª posição')


