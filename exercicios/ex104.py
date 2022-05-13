def leiaInt(inputN):
    while True:
        n = input(inputN)
        if n.isnumeric():
            n = int(n)
            break
        else: 
            print('\033[0;91m ERRO! Digite um número inteiro válido.\033[0m')
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')