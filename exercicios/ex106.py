def ajuda(função):
        print('\033[1;44m~~' * 20)
        print(f'\033[1;44m     Acessando comando {função}     ')
        print('\033[1;44m~~' * 20)
        help(função)

def titulo():
    k


while True:
    resp = input('Função ou Biblioteca > ').upper().strip()
    if resp == 'FIM':
            break
    else:
        ajuda(resp)
