locadora = list()
filme1 = {'título': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
filme2 = {'título': 'Avengers', 'ano': '2011', 'diretor': 'Joss Whedon'}
filme3 = {'título': 'Matrix', 'ano': '1999', 'diretor': 'Wachowski'}
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora[1]['diretor'])

print('-=' * 30)

print(locadora[2]['título'])

print('-=' * 30)

for k, v in filme1.items():
    print(f'O {k} do filme 1 é {v}')
print('-=' * 30)
for k, v in filme2.items():
    print(f'O {k} do filme 2 é {v}')
print('-=' * 30)
for k, v in filme3.items():
    print(f'O {k} do filme 3 é {v}')
print('-=' * 30)

print('<->' * 20)

for e in locadora:
    for k, v in e.items():
        print(f'O {k} é {v}')
    print('-=' * 30)
