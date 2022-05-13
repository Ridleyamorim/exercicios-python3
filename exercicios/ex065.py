seguir = 'S'
cont = soma = n = 0
while seguir != 'N':
    maior = n
    if seguir == 'S' or seguir == 'N':
        n = int(input('Digite um número: '))
        seguir = input('Quer continuar? [S/N] ').upper().strip()
        cont += 1
        soma += n
        if n > maior:
            maior = n
        else:
            menor = n
    else:
        print('Opção inválida, tente novamente!')
        seguir = input('Quer continuar? [S/N] ').upper().strip()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
