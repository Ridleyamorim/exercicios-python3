from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim: 
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont -= passo
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)