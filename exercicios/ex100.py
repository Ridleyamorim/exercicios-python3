def sortear(lista):
    from time import sleep
    from random import randint
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 20) 
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteados = list()
sortear(sorteados)
somaPar(sorteados)

    