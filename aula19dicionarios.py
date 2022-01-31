pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': '38'}
del pessoas['sexo']
pessoas['peso'] = 86
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k in pessoas.items():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

print(pessoas['nome'])
print(pessoas['idade'])


print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
