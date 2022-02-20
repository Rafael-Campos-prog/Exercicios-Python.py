from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analizando os valores passados...', flush=True)
    sleep(1.5)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.8)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.', flush=True)
    sleep(2)
    print(f'O maior valor informado foi {maior}.', flush=True)
    sleep(2)
    print('-=' * 20, flush=True)
    sleep(2)


# Programa principal
maior(2, 9, 4, 5, 7, 11)
maior(4, 2, 0)
maior(9, 3)
maior()
print('<< FIM >>')
