palavras =('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'estudar', 'praticar',
           'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra\033[32m{p.upper()}\033[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
