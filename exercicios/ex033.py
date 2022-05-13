pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))
'''if pri > seg and pri > ter and seg > ter:
    print('O maior valor digitado foi {}'.format(pri))
    print('O menor valor digitado foi {}'.format(ter))
elif pri > seg and pri > ter and ter > seg:
    print('O maior valor digitado foi {}'.format(pri))
    print('O menor valor digitado foi {}'.format(seg))
elif seg > pri and seg > ter and pri > ter:
    print('O maior valor digitado foi {}'.format(seg))
    print('O menor valor digitado foi {}'.format(ter))
elif seg > pri and seg > ter and ter > pri:
    print('O maior valor digitado foi {}'.format(seg))
    print('O menor valor digitado foi {}'.format(pri))
elif ter > pri and ter > seg and pri > seg:
    print('O maior valor digitado foi {}'.format(ter))
    print('O menor valor digitado foi {}'.format(seg))
elif ter > pri and ter > seg and seg > pri:
    print('O maior valor digitado foi {}'.format(ter))
    print('O menor valor digitado foi {}'.format(pri))'''

# Verificando qual é o menor
menor = pri
if seg < ter and seg < ter:
    menor = seg
if ter < pri and ter < seg:
    menor = ter
# Verificando qual é o maior 
maior = pri
if seg > pri and seg > ter:
    maior = seg
if ter > pri and ter > seg:
    maior = ter
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

