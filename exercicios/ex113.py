def leiaInt(inputInt):
    while True:
        try:
            n_int = int(input(inputInt))
        except:
            print('\033[0;91m ERRO! Digite um número inteiro válido.\033[0m')
        else: 
            break
    return n_int


def leiaFloat(inputFloat):
    while True:
        try:
            n_float = float(input(inputFloat))
        except:
            print('\033[0;91m ERRO! Digite um número real válido.\033[0m')
        else:
            break
    return n_float 


nInt = leiaInt('Digite um inteiro: ')
nFloat = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {nInt} e o real foi {nFloat}')