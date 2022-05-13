from random import randint
print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 20)
cont = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    soma = pc + jogador
    if soma % 2 == 0:
        resultado = 'PAR'
        if escolha == 'P':
            placar = 'GANHOU'
        elif escolha == 'I':
           placar = 'PERDEU'
    else:
        resultado = 'ÍMPAR'
        if escolha == 'P':
            placar = 'PERDEU'
        elif escolha == 'I':
           placar = 'GANHOU'
    print('-' * 20)
    print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}, dando {resultado}')
    print('-' * 20)
    print(f'Você {placar}')
    if placar == 'PERDEU':
        break
    cont += 1
print('-=-' * 20)
print(f'GAME OVER! Você venceu {cont} vezes')
