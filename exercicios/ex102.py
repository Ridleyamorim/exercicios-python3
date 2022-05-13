def fatorial(n, show=False):
    """[Calcula o fatorial de um número ]

    Args:
        n ([type]): [o número a ser calculado]
        show (bool, optional): [Mostrar ou não a conta]. Defaults to False.

    Returns:
        [type]: [o valor da conta fatorial de um número]
    """
    fat = 1
    for num in range(n, 0, -1):
        fat *= num
        if show == True:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            else: 
                print(' = ', end='')
    return fat


#print(fatorial(5, True))
help(fatorial)