a1 = float(input('Primeiro aluno: '))
a2 = float(input('Segundo aluno: '))
media = (a1 + a2)/2
if media >= 6:
    situação = 'APROVADO'
elif media < 6:
    situação = 'REPROVADO'
print(' Tirando {} e {}, a média do aluno é {}.\n O aluno está {}.'.format(a1, a2, media, situação)) 