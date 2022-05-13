from time import sleep

def analisar(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    maior = 0
    for i, c in enumerate(num):
        sleep(0.4)
        print(f'{c} ', end='', flush=True)
        if i == 0:
            maior = c
        else: 
            if c > maior:
                maior = c
    total = len(num)
    print(f'Foram informados {total} valores ao todo\nO maior valor informado foi {maior}')


analisar(15, 6, 11, 0, 9, 21, 3, 7)
analisar(2, 9, 4, 5, 7, 1)
analisar(4, 7, 0)
analisar(1, 2)
analisar(6)
analisar()
