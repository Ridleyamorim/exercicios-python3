from datetime import date
today = date.today().year
underAge = 0
overAge = 0
for i in range (1, 8):
    birth = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    yearsOld = today - birth
    if yearsOld < 18:
        underAge += 1
    else:
        overAge += 1
print(f'Ao todo tivemos {overAge} pessoas maiores de idade\nE também tivemos {underAge} pessoas menores de idade.')