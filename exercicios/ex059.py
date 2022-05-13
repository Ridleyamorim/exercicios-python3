from time import sleep
firstNumber = int(input('Primeiro valor: '))
secondNumber = int(input('Segundo valor: '))
selectNumber = 0
while selectNumber != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    selectNumber = int(input('Qual é a sua opção? '))
    if selectNumber == 1:
        sum = firstNumber + secondNumber
        print(f'A soma entre {firstNumber} + {secondNumber} é igual a {sum}')
    elif selectNumber == 2:
        multiplication = firstNumber * secondNumber
        print(f'O resultado de {firstNumber} x {secondNumber} é {multiplication}')
    elif selectNumber == 3:
        if firstNumber == secondNumber:
            print('Os valores são iguais')
        elif firstNumber > secondNumber:
            print(f'Entre {firstNumber} e {secondNumber} o maior é {firstNumber}')
        else:
            print(f'Entre {firstNumber} e {secondNumber} o maior é {secondNumber}')
    elif selectNumber == 4:
        firstNumber = int(input('Primeiro valor: '))
        secondNumber = int(input('Segundo valor: '))
    elif selectNumber == 5:
        print('Finalizando...')
    else:
        print('Operação inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Programa encerrado com sucesso, volte sempre!')

    