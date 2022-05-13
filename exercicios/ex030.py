n = float(input('Me diga um número qualquer: '))
div = n%2

if div == 0:
    store = 'PAR' 
else:
    store = 'IMPAR'

print('O número {:.0f} é {}'.format(n, store))