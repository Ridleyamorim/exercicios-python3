print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
first = int(input('Primeiro termos: '))
jump = int(input('Razão: '))
ten = first + (10 - 1) * jump
for c in range(first, ten + jump, jump):
    print(c, end = ' ')
print('ACABOU, É TETRAAAAA!')