from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 20)

#Programa principal
maior(2, 9, 4, 5, 7, 11)
maior(4, 2, 0)
maior(9, 3)
maior()
