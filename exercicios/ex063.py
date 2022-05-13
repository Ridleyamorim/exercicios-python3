#EXERCÍCIO FIBONACCI
print('-' * 26)
print('Sequência de Fibonacci')
print('-' * 26)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3 #é 3 porque já temos os 2 termos iniciais (t1 e t2)
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
    
