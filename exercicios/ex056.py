#exercio ficou pela metade porque precisei acelerar estudos, completa-lo depois pra treinar!!
soma = 0
number = 0
for p in range (1, 5):
    print('-' * 5, f'{p}ª PESSOA', '-' * 5)
    name = input('Nome: ').upper
    age = int(input('Idade: '))
    gender = input('M/F: ').upper
    soma += age
    if gender == 'F' and age < 20:
        number += 1
    if gender == 'M':
        older = age
        
average = soma / 4


  